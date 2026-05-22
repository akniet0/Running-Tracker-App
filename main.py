from typing import List

from models.runner import Runner

from storage.file_manager import FileManager

from helpers.ui_helpers import header

from actions.menu_actions import (
    add_runner,
    add_run,
    set_goal,
    show_runner,
    show_comparison,
    save_files
)


def main():

    runners: List[Runner] = FileManager.load_csv()

    if runners:
        print(
            f"\n  [OK] Loaded {len(runners)} "
            f"runner(s) from previous session."
        )
    else:
        print("\n  No saved data found. Starting fresh.")

    menu = {
        "1": ("Add runner", lambda: add_runner(runners)),
        "2": ("Add run session", lambda: add_run(runners)),
        "3": ("Set goal", lambda: set_goal(runners)),
        "4": ("View runner", lambda: show_runner(runners)),
        "5": ("Compare runners", lambda: show_comparison(runners)),
        "6": ("Save to files", lambda: save_files(runners)),
        "0": ("Quit", None),
    }

    while True:

        header("RUNNING APP")

        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")

        print()

        choice = input("  Choose: ").strip()

        if choice == "0":
            save_files(runners)
            print("\n  Goodbye!\n")
            break

        elif choice in menu:
            _, action = menu[choice]
            action()

        else:
            print("  Invalid option, try again.")

        input("\n  Press Enter to continue...")


if __name__ == "__main__":
    main()