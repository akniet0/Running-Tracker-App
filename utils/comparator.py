from typing import List, Optional

from models.runner import Runner


class Comparator:

    @staticmethod
    def champion(runners: List[Runner]) -> Optional[Runner]:
        return max(runners, key=lambda r: r.total_km(), default=None)

    @staticmethod
    def compare_progress(runners: List[Runner]) -> str:

        if not runners:
            return "  No runners to compare."

        lines = [
            f"\n  {'Name':<14} {'Total km':>9} {'Runs':>6} {'Avg pace':>10}"
        ]

        lines.append("  " + "-" * 42)

        for r in sorted(runners, key=lambda x: x.total_km(), reverse=True):

            lines.append(
                f"  {r.name:<14} {r.total_km():>9} "
                f"{r.total_runs():>6} "
                f"{r.average_pace():>8} m/km"
            )

        return "\n".join(lines)

    @staticmethod
    def compare_vs_goals(runners: List[Runner]) -> str:

        lines = ["\n  ── Goal progress ──"]

        for r in runners:
            lines.append(f"  {r.name}: {r.goal_progress()}")

        return "\n".join(lines)