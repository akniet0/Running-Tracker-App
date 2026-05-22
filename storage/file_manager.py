import csv
import os
from datetime import datetime
from typing import List, Optional

from models.runner import Runner
from models.run_session import RunSession


class FileManager:
    DATA_FOLDER = "data"

    CSV_FILE = os.path.join(DATA_FOLDER, "runners.csv")
    TXT_FILE = os.path.join(DATA_FOLDER, "report.txt")

    @staticmethod
    def ensure_data_folder():
        os.makedirs(FileManager.DATA_FOLDER, exist_ok=True)

    @staticmethod
    def save_csv(runners: List[Runner]) -> None:
        with open(FileManager.CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            writer.writerow([
                "runner_name",
                "age",
                "date",
                "distance_km",
                "time_min",
                "pace"
            ])

            for r in runners:
                for s in r.runs:
                    writer.writerow([
                        r.name,
                        r.age,
                        s.run_date,
                        s.distance_km,
                        s.time_min,
                        s.pace
                    ])

        print(f"\n  [OK] Saved to {FileManager.CSV_FILE}")

    @staticmethod
    def load_csv() -> List[Runner]:
        runners = {}

        if not os.path.exists(FileManager.CSV_FILE):
            return []

        with open(FileManager.CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                name = row["runner_name"]

                if name not in runners:
                    runners[name] = Runner(name, int(row["age"]))

                session = RunSession(
                    row["date"],
                    float(row["distance_km"]),
                    float(row["time_min"])
                )

                runners[name].add_run(session)

        return list(runners.values())

    @staticmethod
    def save_txt(runners: List[Runner], champion: Optional[Runner]) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        with open(FileManager.TXT_FILE, "w", encoding="utf-8") as f:
            f.write("=" * 45 + "\n")
            f.write(f"  RUNNING APP REPORT — {timestamp}\n")
            f.write("=" * 45 + "\n\n")

            for r in runners:
                f.write(r.summary() + "\n")
                f.write("-" * 35 + "\n")

            f.write("\nCHAMPION\n")

            if champion:
                f.write(f"  {champion.name} — {champion.total_km()} km\n")
            else:
                f.write("  No runners yet.\n")

        print(f"  [OK] Saved to {FileManager.TXT_FILE}")