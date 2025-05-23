"""Interaction class for capturing and finalizing agent conversations."""

from typing import List, Dict, Optional


class Interaction:
    """Represents a completed interaction with an agent."""
    
    def __init__(self, agent, runtime, accumulator_instruction: Optional[str] = None):
        """Initialize an interaction.
        
        Args:
            agent: The agent that had the interaction
            runtime: The runtime that executed the interaction
            accumulator_instruction: Optional instruction for how to process/accumulate the conversation
        """
        # Validate required inputs
        if agent is None:
            raise ValueError("Agent cannot be None")
        if runtime is None:
            raise ValueError("Runtime cannot be None")
        
        # Validate optional accumulator instruction if provided
        if accumulator_instruction is not None:
            if not isinstance(accumulator_instruction, str) or not accumulator_instruction.strip():
                raise ValueError("Accumulator instruction must be a non-empty string if provided")
        
        self.agent = agent
        self.runtime = runtime
        self.accumulator_instruction = accumulator_instruction
        # Capture the conversation history at the time of creation
        self.conversation_history = list(agent.history)
    
    def finalize(self) -> Optional[str]:
        """Finalize the interaction using the accumulator instruction.
        
        Returns:
            The accumulated/extracted result if accumulator instruction was provided, None otherwise
        """
        # If no accumulator instruction, return None
        if self.accumulator_instruction is None:
            return None
        
        # Create an accumulator agent
        accumulator = self.runtime.create_agent(
            name=f"{self.agent.name} - Accumulator",
            instruction=self.accumulator_instruction
        )
        
        # Format the conversation
        conversation_text = "\n".join([
            f"{msg['role']}: {msg['content']}" 
            for msg in self.conversation_history
        ])
        
        # Get the accumulated result
        result = accumulator.send(
            f"Process this conversation:\n\n{conversation_text}",
            add_to_history=False
        )
        
        return result
    
    def get_conversation(self) -> List[Dict[str, str]]:
        """Get the raw conversation history."""
        return self.conversation_history
    
    def get_transcript(self) -> str:
        """Get a formatted transcript of the conversation."""
        return "\n".join([
            f"{msg['role']}: {msg['content']}" 
            for msg in self.conversation_history
        ])