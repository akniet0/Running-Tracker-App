from datetime import datetime
from typing import List

from helpers.ui_helpers import (
    header,
    ask_float,
    ask_int,
    pick_runner
)

from models.runner import Runner
from models.run_session import RunSession
from models.goal import Goal

from utils.comparator import Comparator
from storage.file_manager import FileManager


def add_runner(runners: List[Runner]):

    header("ADD RUNNER")

    name = input("  Name : ").strip()

    if not name:
        print("  Name cannot be empty.")
        return

    age = ask_int("  Age : ")

    runners.append(Runner(name, age))

    print(f"\n  [OK] Runner '{name}' added!")


def add_run(runners: List[Runner]):

    header("ADD RUN SESSION")

    runner = pick_runner(runners)

    if not runner:
        return

    today = datetime.now().strftime("%Y-%m-%d")

    date_input = input(f"  Date [{today}]: ").strip() or today

    distance = ask_float("  Distance (km): ")
    time_min = ask_float("  Time (minutes): ")

    runner.add_run(RunSession(date_input, distance, time_min))

    print(f"\n  [OK] Run added for {runner.name}!")


def set_goal(runners: List[Runner]):

    header("SET GOAL")

    runner = pick_runner(runners)

    if not runner:
        return

    target = ask_float("  Target distance (km): ")

    deadline = input("  Deadline (YYYY-MM-DD): ").strip()

    runner.set_goal(Goal(target, deadline))

    print(f"\n  [OK] Goal set for {runner.name}!")


def show_runner(runners: List[Runner]):

    header("RUNNER PROFILE")

    runner = pick_runner(runners)

    if not runner:
        return

    print()
    print(runner.summary())

    if runner.runs:
        print("\n  -- All runs --")

        for s in runner.runs:
            print(s)


def show_comparison(runners: List[Runner]):

    header("COMPARE RUNNERS")

    print(Comparator.compare_progress(runners))
    print(Comparator.compare_vs_goals(runners))

    champ = Comparator.champion(runners)

    if champ:
        print(f"\n  Champion: {champ.name} ({champ.total_km()} km)")


def save_files(runners: List[Runner]):

    header("SAVE FILES")

    if not runners:
        print("  No data to save yet.")
        return

    champ = Comparator.champion(runners)

    FileManager.save_csv(runners)
    FileManager.save_txt(runners, champ)