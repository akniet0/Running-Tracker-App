from typing import List, Optional

from models.run_session import RunSession
from models.goal import Goal


class Runner:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.runs: List[RunSession] = []
        self.goal: Optional[Goal] = None

    def total_km(self) -> float:
        return round(sum(r.distance_km for r in self.runs), 2)

    def total_runs(self) -> int:
        return len(self.runs)

    def average_pace(self) -> float:
        paces = [r.pace for r in self.runs if r.distance_km > 0]
        return round(sum(paces) / len(paces), 2) if paces else 0.0

    def best_run(self):
        return max(self.runs, key=lambda r: r.distance_km, default=None)

    def goal_progress(self) -> str:
        if not self.goal:
            return "No goal set"

        done = self.total_km()
        pct = min(round(done / self.goal.target_km * 100, 1), 100)

        status = (
            "✓ Achieved!"
            if self.goal.is_achieved(done)
            else f"{pct}% done"
        )

        return f"{done}/{self.goal.target_km} km — {status}"

    def add_run(self, session: RunSession):
        self.runs.append(session)

    def set_goal(self, goal: Goal):
        self.goal = goal

    def summary(self) -> str:
        lines = [
            f"  Runner : {self.name} (age {self.age})",
            f"  Runs   : {self.total_runs()}",
            f"  Total  : {self.total_km()} km",
            f"  Pace   : {self.average_pace()} min/km",
        ]

        best = self.best_run()

        if best:
            lines.append(f"  Best   : {best}")

        lines.append(f"  Goal   : {self.goal_progress()}")

        return "\n".join(lines)