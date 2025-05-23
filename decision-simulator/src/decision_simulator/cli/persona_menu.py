"""Persona management menu for decision simulator."""

from typing import Dict
from ..personas import Persona
from ..agent import Agent


def manage_personas(personas: Dict[str, Persona], runtime):
    """Manage personas.

    Args:
        personas: Dictionary storing personas by name
        runtime: AgentRuntime instance
    """
    while True:
        print("\n=== Persona Management ===")
        print("[c] Create new persona")
        print("[l] List all personas")
        print("[e] Edit persona")
        print("[d] Delete persona")
        print("[b] Back to main menu")
        print("\nEnter your choice: ", end="")

        choice = input().strip().lower()

        if choice == "c":
            create_persona_with_ai(personas, runtime)
        elif choice == "l":
            list_personas(personas, runtime)
        elif choice == "e":
            print("\n[Edit Persona - Coming Soon]")
            input("Press Enter to continue...")
        elif choice == "d":
            delete_persona(personas)
        elif choice == "b":
            break
        else:
            print("\nInvalid choice. Please try again.")


def create_persona_with_ai(personas: Dict[str, Persona], runtime):
    """Create a persona using AI-assisted interview.

    Args:
        personas: Dictionary storing personas by name
        runtime: AgentRuntime instance
    """
    try:
        # First ask for the name
        print("\n=== AI-Assisted Persona Creation ===")
        name = input("Enter a name for this persona: ").strip()
        if not name:
            print("Name is required!")
            return
            
        if name in personas:
            overwrite = input(f"Persona '{name}' already exists. Overwrite? (y/n): ").strip().lower()
            if overwrite != "y":
                print("Persona creation cancelled.")
                return
        
        # Create persona generator agent inline
        generator = runtime.create_agent(
            name="Persona Generator",
            instruction=f"""You are a persona creation assistant helping users design detailed, realistic personas for decision simulation.

The user is creating a persona named: {name}

Your job is to:
1. Interview the user to gather comprehensive information about the persona
2. Ask probing questions to flesh out personality, background, goals, and other characteristics
3. Help them think deeply about what makes this persona unique
4. Continue gathering information until the user explicitly says they are done

Focus especially on:
- Getting a clear, specific background story
- Understanding multiple personality traits (not just adjectives, but behavioral patterns)
- Identifying concrete goals and motivations
- Capturing their communication style with examples
- Any unique quirks or characteristics"""
        )
        
        print(f"\nCreating persona: {name}")
        print("I'll interview you to build out this persona.")
        print("Type 'exit' when you're done.\n")
        
        # Run interactive interview with initial question
        initial_question = f"Let's start creating {name}. Can you tell me about their background? Where are they from, what's their history, and what experiences have shaped who they are?"
        generator.interact(initial_question=initial_question)
        
        # After interview, create structured data
        structurer = runtime.create_agent(
            name="Data Structurer",
            instruction="""You are a data extraction expert. Your job is to extract structured persona data from conversation history.

You must extract:
- name (string)
- background (string)
- personality_traits (list of strings)
- goals (list of strings)
- communication_style (optional string)
- expertise (optional string)
- quirks (optional string)
- values (optional dict)

Return ONLY valid JSON with these fields."""
        )
        
        # Get conversation summary
        conversation = "\n".join([
            f"{msg['role']}: {msg['content']}" 
            for msg in generator.history
        ])
        
        json_response = structurer.send(
            f"""Based on this conversation about {name}, extract structured persona data:

{conversation}

Remember: name must be "{name}", personality_traits and goals must be lists.""",
            add_to_history=False
        )
        
        # Parse and create persona
        import json
        persona_data = json.loads(json_response)
        persona = Persona(**persona_data)
        
        personas[persona.name] = persona
        print(f"\nPersona '{persona.name}' added successfully!")
        
        # Offer to chat
        chat_now = input("\nWould you like to chat with this persona now? (y/n): ").strip().lower()
        if chat_now == "y":
            chat_with_persona(persona, runtime)
            
    except Exception as e:
        print(f"\nError creating persona: {e}")
        input("Press Enter to continue...")


def list_personas(personas: Dict[str, Persona], runtime):
    """List all personas with selection option.

    Args:
        personas: Dictionary storing personas by name
        runtime: AgentRuntime instance
    """
    print("\n=== All Personas ===")
    if not personas:
        print("No personas created yet.")
        input("\nPress Enter to continue...")
        return

    # Show numbered list
    persona_list = list(personas.items())
    for i, (name, persona) in enumerate(persona_list, 1):
        print(f"{i}. {persona.summary()}")

    print("\nEnter persona number to view details (or press Enter to go back): ", end="")
    choice = input().strip()

    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(persona_list):
            name, persona = persona_list[idx]
            show_persona_detail(name, persona, runtime)
        else:
            print("Invalid selection.")
            input("Press Enter to continue...")


def show_persona_detail(name: str, persona: Persona, runtime):
    """Show detailed view of a persona with options.

    Args:
        name: The persona's name
        persona: The Persona object
        runtime: AgentRuntime instance
    """
    while True:
        print(f"\n=== Persona: {name} ===")
        print(f"Background: {persona.background}")

        if persona.personality_traits:
            print(f"\nPersonality Traits:")
            for trait in persona.personality_traits:
                print(f"  - {trait}")

        if persona.goals:
            print(f"\nGoals:")
            for goal in persona.goals:
                print(f"  - {goal}")

        if persona.communication_style:
            print(f"\nCommunication Style: {persona.communication_style}")

        if persona.expertise:
            print(f"Expertise: {persona.expertise}")

        if persona.quirks:
            print(f"Quirks: {persona.quirks}")

        if persona.values:
            print(f"\nValues:")
            for key, value in persona.values.items():
                print(f"  - {key}: {value}")

        print("\n[c] Chat with this persona")
        print("[b] Back to persona list")
        print("\nEnter your choice: ", end="")

        choice = input().strip().lower()

        if choice == "c":
            chat_with_persona(persona, runtime)
        elif choice == "b":
            break
        else:
            print("\nInvalid choice. Please try again.")


def chat_with_persona(persona: Persona, runtime):
    """Start a chat session with a persona.
    
    Args:
        persona: The Persona to chat with
        runtime: AgentRuntime instance
    """
    print(f"\nPreparing chat with {persona.name}...")
    
    # Create character builder agent inline
    character_builder = runtime.create_agent(
        name="Character Builder",
        instruction="""You are an expert character designer. Take the given persona data and create a comprehensive, detailed character description that an AI can embody convincingly.

Include speech patterns, behavioral quirks, decision-making style, emotional responses, and how they express their traits in conversation."""
    )
    
    # Build character description
    print("Building character profile...")
    character_desc = character_builder.send(
        f"Create a detailed character description for: {persona.to_dict()}",
        add_to_history=False
    )
    
    # Create prompt synthesizer agent inline
    prompt_synthesizer = runtime.create_agent(
        name="Prompt Synthesizer",
        instruction="""You are an expert at creating system prompts. Combine character descriptions with scenarios into clear, natural prompts that enable authentic roleplay."""
    )
    
    # Synthesize prompt
    print("Preparing conversation...")
    system_prompt = prompt_synthesizer.send(
        f"""Create a system prompt for this character in a casual conversation:

CHARACTER: {character_desc}

SCENARIO: Having a friendly chat with someone who wants to get to know you better.""",
        add_to_history=False
    )
    
    # Create the persona agent
    persona_agent = runtime.create_agent(
        name=persona.name,
        instruction=system_prompt
    )
    
    print(f"\n=== Starting chat with {persona.name} ===")
    print("Type 'exit' to end the conversation.")
    print("-" * 60)
    print()
    
    # Run interactive chat with initial greeting
    initial_greeting = f"Hello! I'm {persona.name}. It's nice to meet you. What would you like to talk about?"
    persona_agent.interact(initial_question=initial_greeting)


def delete_persona(personas: Dict[str, Persona]):
    """Delete a persona.

    Args:
        personas: Dictionary storing personas by name
    """
    if not personas:
        print("\nNo personas to delete.")
        input("Press Enter to continue...")
        return

    print("\n=== Delete Persona ===")
    print("Available personas:")
    for i, name in enumerate(personas.keys(), 1):
        print(f"{i}. {name}")

    name = input("\nEnter persona name to delete (or press Enter to cancel): ").strip()
    if name and name in personas:
        confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
        if confirm == "y":
            del personas[name]
            print(f"Persona '{name}' deleted.")
    elif name:
        print(f"Persona '{name}' not found.")

    input("Press Enter to continue...")