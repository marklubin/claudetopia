"""Agent runtime - the main entry point for agent execution."""

from typing import Optional
from .agent import Agent
from .provider import LLMProvider, LLMConfig
from .interaction import Interaction


class AgentRuntime:
    """Central runtime for managing agent execution."""
    
    def __init__(self, provider: Optional[LLMProvider] = None):
        """Initialize runtime with a provider."""
        if provider is None:
            # Create default provider
            provider = LLMProvider(LLMConfig())
        self.provider = provider
    
    @classmethod
    def create(cls, config: Optional[LLMConfig] = None) -> 'AgentRuntime':
        """Factory method to create runtime with config."""
        if config is None:
            config = LLMConfig()
        provider = LLMProvider(config)
        return cls(provider)
    
    def create_agent(self, name: str, instruction: str) -> Agent:
        """Create an agent instance connected to this runtime."""
        return Agent(name, instruction, self)
    
    def submit(self, agent: Agent, message: str, add_to_history: bool = True) -> str:
        """Submit a message from an agent for execution.
        
        Currently synchronous, but could be async/queued in future.
        """
        # Prepare messages with system prompt
        messages = [
            {"role": "system", "content": agent.instruction}
        ]
        
        # Add existing history
        messages.extend(agent.history)
        
        # Add the current message
        messages.append({"role": "user", "content": message})
        
        # Execute through provider (future: could queue, batch, etc.)
        try:
            response = self.provider.complete(messages)
            
            # Only record history after successful response
            if add_to_history:
                agent.add_message("user", message)
                agent.add_message("assistant", response)
            
            return response
            
        except Exception as e:
            # If request fails, don't record anything in history
            raise RuntimeError(f"Failed to get response from LLM: {e}") from e
    
    def run_interactive_chat(self, agent: Agent, initial_question: Optional[str] = None, accumulator_instruction: Optional[str] = None) -> Interaction:
        """Run an interactive chat session with an agent.
        
        Args:
            agent: The agent to chat with
            initial_question: Optional question to start the conversation
            accumulator_instruction: Optional instruction for processing the conversation
            
        Returns:
            An Interaction object containing the completed conversation
        """
        print(f"\n=== {agent.name} ===")
        print("Type 'exit' to end the conversation.\n")
        
        # Clear history before starting to ensure clean interaction
        start_index = len(agent.history)
        
        # If there's an initial question, ask it first
        if initial_question:
            print(f"{agent.name}: {initial_question}\n")
            # Add the initial question to history as an assistant message
            agent.add_message("assistant", initial_question)
        
        while True:
            try:
                user_input = input("> ").strip()
                if user_input.lower() in ['exit', 'quit']:
                    print(f"\nEnding session with {agent.name}.")
                    break
                
                if not user_input:
                    continue
                    
                response = agent.send(user_input)
                print(f"\n{agent.name}: {response}\n")
                
            except KeyboardInterrupt:
                print(f"\n\nSession interrupted.")
                break
            except Exception as e:
                print(f"\nError: {e}")
                import traceback
                traceback.print_exc()
        
        # Create and return the interaction with just the messages from this session
        interaction = Interaction(agent, self, accumulator_instruction)
        # Update the conversation history to only include messages from this interaction
        interaction.conversation_history = agent.history[start_index:]
        return interaction