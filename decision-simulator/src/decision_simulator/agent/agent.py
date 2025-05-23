"""Agent class for managing conversation state."""

from typing import List, Dict, Optional


class Agent:
    """Agent class that manages conversation state."""
    
    def __init__(self, name: str, instruction: str, runtime):
        # Validate inputs
        if name is None:
            raise ValueError("Agent name cannot be None")
        if instruction is None:
            raise ValueError("Agent instruction cannot be None")
        if runtime is None:
            raise ValueError("Agent runtime cannot be None")
        
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Agent name must be a non-empty string")
        if not isinstance(instruction, str) or not instruction.strip():
            raise ValueError("Agent instruction must be a non-empty string")
        
        self.name = name
        self.instruction = instruction
        self.runtime = runtime
        self.history: List[Dict[str, str]] = []
    
    def send(self, message: str, add_to_history: bool = True) -> str:
        """Send a message through the runtime."""
        return self.runtime.submit(self, message, add_to_history)
    
    def interact(self, initial_question: Optional[str] = None, accumulator_instruction: Optional[str] = None):
        """Start an interactive chat session through the runtime.
        
        Args:
            initial_question: Optional question to start the conversation
            accumulator_instruction: Optional instruction for accumulating/processing the conversation
            
        Returns:
            An Interaction object containing the conversation
        """
        return self.runtime.run_interactive_chat(self, initial_question, accumulator_instruction)
    
    def add_message(self, role: str, content: str):
        """Add a message to history."""
        self.history.append({"role": role, "content": content})
    
    def get_messages(self, include_system: bool = True) -> List[Dict[str, str]]:
        """Get all messages with optional system prompt."""
        messages = []
        if include_system:
            messages.append({"role": "system", "content": self.instruction})
        messages.extend(self.history)
        return messages
    
    def clear_history(self):
        """Clear conversation history."""
        self.history.clear()
    
    def set_instruction(self, instruction: str):
        """Update the system instruction."""
        self.instruction = instruction