"""LLM provider for handling API calls."""

import os
from typing import List, Dict, Optional
from dataclasses import dataclass
from openai import OpenAI


@dataclass
class LLMConfig:
    """Configuration for LLM provider."""
    provider: str = "openai"  # openai, anthropic, etc.
    model: str = "gpt-4"
    api_key: Optional[str] = None
    temperature: float = 0.7
    max_tokens: Optional[int] = None
    # Other provider-specific settings
    
    def __post_init__(self):
        """Set defaults after initialization."""
        if self.api_key is None and self.provider == "openai":
            self.api_key = os.getenv("OPENAI_API_KEY")


class LLMProvider:
    """Handles actual LLM API calls."""
    
    def __init__(self, config: LLMConfig):
        self.config = config
        self._client = None
    
    @property
    def client(self):
        """Lazy initialize client based on provider."""
        if self._client is None:
            if self.config.provider == "openai":
                self._client = OpenAI(api_key=self.config.api_key)
            # Add other providers as needed
            else:
                raise ValueError(f"Unknown provider: {self.config.provider}")
        return self._client
    
    def complete(self, messages: List[Dict[str, str]]) -> str:
        """Make completion call to LLM."""
        if self.config.provider == "openai":
            response = self.client.chat.completions.create(
                model=self.config.model,
                messages=messages,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens
            )
            return response.choices[0].message.content
        else:
            raise ValueError(f"Unknown provider: {self.config.provider}")