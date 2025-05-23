"""Admin console menu for decision simulator."""

from typing import Dict
from ..personas import Persona


def admin_console(personas: Dict[str, Persona]):
    """Admin console for direct entity creation.

    Args:
        personas: Dictionary storing personas by name
    """
    while True:
        print("\n=== Admin Console ===")
        print("[p] Create Persona (Manual)")
        print("[s] Create Scenario (Manual)")
        print("[b] Back to main menu")
        print("\nEnter your choice: ", end="")

        choice = input().strip().lower()

        if choice == "p":
            create_persona_manual(personas)
        elif choice == "s":
            print("\n[Create Scenario Manual - Coming Soon]")
            input("Press Enter to continue...")
        elif choice == "b":
            break
        else:
            print("\nInvalid choice. Please try again.")


def create_persona_manual(personas: Dict[str, Persona]):
    """Create a persona by manually entering each field.

    Args:
        personas: Dictionary storing personas by name
    """
    print("\n=== Manual Persona Creation ===")

    # Get required fields
    name = input("Enter persona name: ").strip()
    if not name:
        print("Name is required!")
        return

    if name in personas:
        print(f"Persona '{name}' already exists!")
        return

    background = input("Enter background/description: ").strip()
    if not background:
        print("Background is required!")
        return

    # Get personality traits
    print(
        "\nEnter personality traits (one per line, press Enter with empty line to finish):"
    )
    personality_traits = []
    while True:
        trait = input("  Trait: ").strip()
        if not trait:
            break
        personality_traits.append(trait)

    # Get goals
    print("\nEnter goals (one per line, press Enter with empty line to finish):")
    goals = []
    while True:
        goal = input("  Goal: ").strip()
        if not goal:
            break
        goals.append(goal)

    # Get optional fields
    print("\nOptional fields (press Enter to skip):")
    communication_style = input("Communication style: ").strip() or None
    expertise = input("Expertise/skills: ").strip() or None
    quirks = input("Quirks/unique behaviors: ").strip() or None

    # Get values
    print("\nEnter values (press Enter with empty key to finish):")
    values = {}
    while True:
        value_key = input("  Value name: ").strip()
        if not value_key:
            break
        value_desc = input(f"  {value_key} description: ").strip()
        if value_desc:
            values[value_key] = value_desc

    # Create persona
    persona = Persona(
        name=name,
        background=background,
        personality_traits=personality_traits,
        goals=goals,
        communication_style=communication_style,
        expertise=expertise,
        values=values if values else None,
        quirks=quirks,
    )

    personas[name] = persona
    print(f"\nPersona '{name}' created successfully!")
    print(f"Summary: {persona.summary()}")
    input("\nPress Enter to continue...")
