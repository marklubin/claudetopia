"""Persona class for decision simulator."""

from dataclasses import dataclass, field
from typing import Dict, Any, Optional, List


@dataclass
class Persona:
    """Pure data representation of a persona."""

    name: str
    background: str
    personality_traits: List[str] = field(default_factory=list)
    goals: List[str] = field(default_factory=list)
    communication_style: Optional[str] = None
    expertise: Optional[str] = None
    values: Optional[Dict[str, Any]] = None
    quirks: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert persona to dictionary for serialization."""
        return {
            "name": self.name,
            "background": self.background,
            "personality_traits": self.personality_traits,
            "goals": self.goals,
            "communication_style": self.communication_style,
            "expertise": self.expertise,
            "values": self.values,
            "quirks": self.quirks,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Persona":
        """Create persona from dictionary."""
        return cls(**data)

    def summary(self) -> str:
        """Get a brief summary of the persona."""
        parts = [f"{self.name}: {self.background}"]
        if self.personality_traits:
            traits = ", ".join(self.personality_traits)
            parts.append(f"Traits: {traits}")
        return " | ".join(parts)
