#!/usr/bin/env python3
"""Main entry point for the decision simulator."""

import os
from typing import Dict
from src.decision_simulator.personas import Persona
from src.decision_simulator.cli import run_main_loop
from src.decision_simulator.utils.error_handler import install_error_handler
from src.decision_simulator.agent import AgentRuntime, LLMConfig

# Global storage for personas (in-memory for now)
personas: Dict[str, Persona] = {}


def main():
    """Main function with CLI loop."""
    # Install the error handler first thing
    install_error_handler()
    
    # Create the agent runtime
    config = LLMConfig(
        provider="openai",
        model="gpt-4",
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.7
    )
    runtime = AgentRuntime.create(config)
    
    # Now run normally with runtime
    run_main_loop(personas, runtime)


if __name__ == "__main__":
    main()
