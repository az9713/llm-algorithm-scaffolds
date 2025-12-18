"""
Claude (Anthropic) LLM provider implementation.
"""

import asyncio
import time
from typing import Any

from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from ..config import get_settings
from .base import (
    AuthenticationError,
    InvalidRequestError,
    LLMError,
    LLMProvider,
    LLMRequest,
    LLMResponse,
    RateLimitError,
)

try:
    import anthropic
    from anthropic import APIError, APIStatusError, RateLimitError as AnthropicRateLimitError
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    anthropic = None


class ClaudeProvider(LLMProvider):
    """Anthropic Claude LLM provider."""

    def __init__(self, api_key: str | None = None):
        """
        Initialize the Claude provider.

        Args:
            api_key: Anthropic API key. If not provided, uses settings.
        """
        settings = get_settings()
        self._api_key = api_key or settings.anthropic_api_key
        self._client: Any = None
        self._async_client: Any = None

    @property
    def provider_name(self) -> str:
        return "anthropic"

    @property
    def default_model(self) -> str:
        return get_settings().active_model

    def _get_client(self) -> Any:
        """Get or create the synchronous client."""
        if not ANTHROPIC_AVAILABLE:
            raise LLMError("anthropic package not installed", provider=self.provider_name)
        if not self._client:
            self._client = anthropic.Anthropic(api_key=self._api_key)
        return self._client

    def _get_async_client(self) -> Any:
        """Get or create the async client."""
        if not ANTHROPIC_AVAILABLE:
            raise LLMError("anthropic package not installed", provider=self.provider_name)
        if not self._async_client:
            self._async_client = anthropic.AsyncAnthropic(api_key=self._api_key)
        return self._async_client

    def is_available(self) -> bool:
        """Check if Claude is available."""
        return ANTHROPIC_AVAILABLE and bool(self._api_key)

    def _handle_error(self, e: Exception, model: str) -> None:
        """Convert Anthropic errors to our error types."""
        if not ANTHROPIC_AVAILABLE:
            raise LLMError(str(e), provider=self.provider_name, model=model)

        if isinstance(e, AnthropicRateLimitError):
            raise RateLimitError(
                str(e),
                provider=self.provider_name,
                model=model,
                status_code=429,
            )
        elif isinstance(e, APIStatusError):
            if e.status_code == 401:
                raise AuthenticationError(
                    str(e),
                    provider=self.provider_name,
                    model=model,
                    status_code=401,
                )
            elif e.status_code == 400:
                raise InvalidRequestError(
                    str(e),
                    provider=self.provider_name,
                    model=model,
                    status_code=400,
                )
            else:
                raise LLMError(
                    str(e),
                    provider=self.provider_name,
                    model=model,
                    status_code=e.status_code,
                )
        elif isinstance(e, APIError):
            raise LLMError(str(e), provider=self.provider_name, model=model)
        else:
            raise LLMError(str(e), provider=self.provider_name, model=model)

    async def generate(
        self,
        request: LLMRequest,
        model: str | None = None,
    ) -> LLMResponse:
        """Generate a response from Claude."""
        if not self.is_available():
            raise AuthenticationError(
                "Claude not available: API key not configured",
                provider=self.provider_name,
            )

        model = model or self.default_model
        client = self._get_async_client()

        messages = [{"role": "user", "content": request.prompt}]
        kwargs: dict[str, Any] = {
            "model": model,
            "max_tokens": request.max_tokens,
            "temperature": request.temperature,
            "messages": messages,
        }

        if request.system_prompt:
            kwargs["system"] = request.system_prompt

        start_time = time.perf_counter()
        try:
            response = await client.messages.create(**kwargs)
        except Exception as e:
            self._handle_error(e, model)

        elapsed_ms = (time.perf_counter() - start_time) * 1000

        content = ""
        if response.content:
            content = response.content[0].text

        return LLMResponse(
            content=content,
            model=response.model,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
            latency_ms=elapsed_ms,
            raw_response=response,
        )

    async def generate_with_retry(
        self,
        request: LLMRequest,
        model: str | None = None,
        max_retries: int = 3,
        retry_delay: float = 1.0,
    ) -> LLMResponse:
        """Generate a response with automatic retry."""
        last_error: Exception | None = None

        for attempt in range(max_retries):
            try:
                return await self.generate(request, model)
            except RateLimitError as e:
                last_error = e
                delay = retry_delay * (2 ** attempt)
                await asyncio.sleep(delay)
            except (AuthenticationError, InvalidRequestError):
                raise
            except LLMError as e:
                last_error = e
                if attempt < max_retries - 1:
                    delay = retry_delay * (2 ** attempt)
                    await asyncio.sleep(delay)

        raise last_error or LLMError("All retries failed", provider=self.provider_name)

    def generate_sync(
        self,
        request: LLMRequest,
        model: str | None = None,
    ) -> LLMResponse:
        """Synchronous version of generate (for testing convenience)."""
        return asyncio.run(self.generate(request, model))


def get_claude_provider(api_key: str | None = None) -> ClaudeProvider:
    """Factory function to create a Claude provider."""
    return ClaudeProvider(api_key)
