"""
Abstract base class for LLM providers.

Defines the interface that all LLM integrations must implement.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class LLMResponse:
    """Response from an LLM provider."""

    content: str
    """The text content of the response."""

    model: str
    """The model that generated the response."""

    input_tokens: int = 0
    """Number of tokens in the prompt."""

    output_tokens: int = 0
    """Number of tokens in the response."""

    latency_ms: float = 0.0
    """Time taken for the API call in milliseconds."""

    timestamp: datetime = field(default_factory=datetime.now)
    """When the response was generated."""

    raw_response: Any = None
    """Raw response object from the provider (for debugging)."""

    @property
    def total_tokens(self) -> int:
        """Total tokens used (input + output)."""
        return self.input_tokens + self.output_tokens

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "content": self.content,
            "model": self.model,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "total_tokens": self.total_tokens,
            "latency_ms": self.latency_ms,
            "timestamp": self.timestamp.isoformat(),
        }


@dataclass
class LLMRequest:
    """Request to send to an LLM provider."""

    prompt: str
    """The prompt to send."""

    system_prompt: str = ""
    """Optional system prompt."""

    temperature: float = 0.0
    """Temperature for response generation."""

    max_tokens: int = 4096
    """Maximum tokens in response."""

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "prompt": self.prompt,
            "system_prompt": self.system_prompt,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }


class LLMProvider(ABC):
    """Abstract base class for LLM providers."""

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Return the name of this provider (e.g., 'anthropic', 'openai')."""
        pass

    @property
    @abstractmethod
    def default_model(self) -> str:
        """Return the default model for this provider."""
        pass

    @abstractmethod
    async def generate(
        self,
        request: LLMRequest,
        model: str | None = None,
    ) -> LLMResponse:
        """
        Generate a response from the LLM.

        Args:
            request: The request containing prompt and parameters.
            model: Optional model override (uses default if not specified).

        Returns:
            LLMResponse containing the generated content and metadata.

        Raises:
            LLMError: If the API call fails.
        """
        pass

    @abstractmethod
    async def generate_with_retry(
        self,
        request: LLMRequest,
        model: str | None = None,
        max_retries: int = 3,
        retry_delay: float = 1.0,
    ) -> LLMResponse:
        """
        Generate a response with automatic retry on failure.

        Args:
            request: The request containing prompt and parameters.
            model: Optional model override.
            max_retries: Maximum number of retry attempts.
            retry_delay: Initial delay between retries (exponential backoff).

        Returns:
            LLMResponse containing the generated content and metadata.

        Raises:
            LLMError: If all retries fail.
        """
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """Check if this provider is available (API key configured, etc.)."""
        pass


class LLMError(Exception):
    """Base exception for LLM-related errors."""

    def __init__(
        self,
        message: str,
        provider: str = "",
        model: str = "",
        status_code: int | None = None,
    ):
        super().__init__(message)
        self.provider = provider
        self.model = model
        self.status_code = status_code


class RateLimitError(LLMError):
    """Raised when rate limits are hit."""
    pass


class AuthenticationError(LLMError):
    """Raised when authentication fails."""
    pass


class InvalidRequestError(LLMError):
    """Raised when the request is invalid."""
    pass
