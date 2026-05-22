from typing import List, Optional

from models.runner import Runner


def divider():
    print("\n" + "-" * 40)


def header(title: str):
    divider()
    print(f"  {title}")
    divider()


def ask_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Please enter a number.")


def ask_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Please enter a whole number.")


def pick_runner(runners: List[Runner]) -> Optional[Runner]:

    if not runners:
        print("  No runners yet. Add one first.")
        return None

    print()

    for i, r in enumerate(runners, 1):
        print(f"  {i}. {r.name} — {r.total_km()} km total")

    choice = ask_int("  Pick runner number: ")

    if 1 <= choice <= len(runners):
        return runners[choice - 1]

    print("  Invalid choice.")
    return None