"""Main menu for decision simulator."""

from typing import Dict
from ..personas import Persona

# Import menu functions
from .admin_menu import admin_console
from .persona_menu import manage_personas
from .scenario_menu import manage_scenarios
from .simulation_menu import run_simulation


def display_menu():
    """Display the main menu."""
    print("\n=== Decision Simulator ===")
    print("[a] Admin Console")
    print("[p] Manage Personas")
    print("[s] Manage Scenarios")
    print("[r] Run Simulation")
    print("[q] Quit")
    print("\nEnter your choice: ", end="")


def run_main_loop(personas: Dict[str, Persona], runtime):
    """Run the main CLI loop.

    Args:
        personas: Dictionary storing personas by name
        runtime: AgentRuntime instance
    """
    print("Welcome to Decision Simulator!")
    print("Use the letter commands shown in brackets to navigate.")

    while True:
        display_menu()

        try:
            choice = input().strip().lower()

            if choice == "a":
                admin_console(personas)
            elif choice == "p":
                manage_personas(personas, runtime)
            elif choice == "s":
                manage_scenarios()
            elif choice == "r":
                run_simulation(personas)
            elif choice == "q":
                print("\nThank you for using Decision Simulator. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please use a, p, s, r, or q.")
        except KeyboardInterrupt:
            print("\n\nExiting Decision Simulator...")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            input("Press Enter to continue...")
