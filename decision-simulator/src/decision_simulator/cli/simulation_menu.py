"""Simulation menu for decision simulator."""

from typing import Dict
from ..personas import Persona


def run_simulation(personas: Dict[str, Persona]):
    """Run a simulation.

    Args:
        personas: Dictionary storing personas by name
    """
    while True:
        print("\n=== Run Simulation ===")
        print("[s] Select scenario")
        print("[p] Select personas")
        print("[r] Run with current selection")
        print("[v] View last results")
        print("[b] Back to main menu")
        print("\nEnter your choice: ", end="")

        choice = input().strip().lower()

        if choice == "s":
            print("\n[Select Scenario - Coming Soon]")
            input("Press Enter to continue...")
        elif choice == "p":
            print("\n[Select Personas - Coming Soon]")
            if personas:
                print("Available personas:")
                for name in personas.keys():
                    print(f"  - {name}")
            else:
                print("No personas available. Create some first!")
            input("Press Enter to continue...")
        elif choice == "r":
            print("\n[Running Simulation - Coming Soon]")
            input("Press Enter to continue...")
        elif choice == "v":
            print("\n[View Results - Coming Soon]")
            input("Press Enter to continue...")
        elif choice == "b":
            break
        else:
            print("\nInvalid choice. Please try again.")
