"""
Configuration management for the verification framework.

Uses pydantic-settings for environment variable loading and validation.
"""

from pathlib import Path
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Verification framework settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="VERIFY_",
        extra="ignore",
    )

    # API Configuration
    anthropic_api_key: str = Field(
        default="",
        description="Anthropic API key for Claude access",
    )

    # Model Selection
    dev_model: str = Field(
        default="claude-3-haiku-20240307",
        description="Model to use during development (cheaper, faster)",
    )
    cert_model: str = Field(
        default="claude-3-opus-20240229",
        description="Model to use for final certification (more capable)",
    )
    current_mode: Literal["dev", "cert"] = Field(
        default="dev",
        description="Current mode: 'dev' uses dev_model, 'cert' uses cert_model",
    )

    # LLM Parameters
    temperature: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Temperature for LLM responses (0 for deterministic)",
    )
    max_tokens: int = Field(
        default=4096,
        ge=1,
        le=100000,
        description="Maximum tokens in LLM response",
    )
    timeout_seconds: int = Field(
        default=120,
        ge=10,
        le=600,
        description="Timeout for LLM API calls in seconds",
    )

    # Retry Configuration
    max_retries: int = Field(
        default=3,
        ge=1,
        le=10,
        description="Maximum retries for failed API calls",
    )
    retry_delay_seconds: float = Field(
        default=1.0,
        ge=0.1,
        le=60.0,
        description="Initial delay between retries (exponential backoff)",
    )

    # Paths
    scaffolds_dir: Path = Field(
        default=Path("scaffolds"),
        description="Directory containing scaffold markdown files",
    )
    results_dir: Path = Field(
        default=Path("verification_results"),
        description="Directory for storing verification results",
    )
    test_cases_dir: Path = Field(
        default=Path("verification_results/data"),
        description="Directory for storing test case JSON files",
    )

    # Test Configuration
    test_cases_per_scaffold: int = Field(
        default=11,
        ge=3,
        le=50,
        description="Number of test cases per scaffold (3 simple + 5 standard + 3 edge)",
    )
    parallel_llm_calls: int = Field(
        default=5,
        ge=1,
        le=20,
        description="Maximum parallel LLM API calls",
    )

    # Caching
    enable_cache: bool = Field(
        default=True,
        description="Enable caching of LLM responses to avoid redundant calls",
    )
    cache_dir: Path = Field(
        default=Path("verification_results/cache"),
        description="Directory for caching LLM responses",
    )

    @property
    def active_model(self) -> str:
        """Return the currently active model based on mode."""
        return self.cert_model if self.current_mode == "cert" else self.dev_model

    def get_scaffolds_path(self) -> Path:
        """Get absolute path to scaffolds directory."""
        if self.scaffolds_dir.is_absolute():
            return self.scaffolds_dir
        return Path(__file__).parent.parent / self.scaffolds_dir

    def get_results_path(self) -> Path:
        """Get absolute path to results directory."""
        if self.results_dir.is_absolute():
            return self.results_dir
        return Path(__file__).parent.parent / self.results_dir

    def ensure_directories(self) -> None:
        """Create required directories if they don't exist."""
        dirs = [
            self.get_results_path(),
            self.get_results_path() / "logs",
            self.get_results_path() / "reports",
            self.get_results_path() / "data",
        ]
        if self.enable_cache:
            dirs.append(self.cache_dir if self.cache_dir.is_absolute()
                       else Path(__file__).parent.parent / self.cache_dir)
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)


# Global settings instance
settings = Settings()


def get_settings() -> Settings:
    """Get the global settings instance."""
    return settings


def reload_settings() -> Settings:
    """Reload settings from environment (useful for testing)."""
    global settings
    settings = Settings()
    return settings
