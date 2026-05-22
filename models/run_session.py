class RunSession:
    def __init__(self, run_date: str, distance_km: float, time_min: float):
        self.run_date = run_date
        self.distance_km = distance_km
        self.time_min = time_min

    @property
    def pace(self) -> float:
        if self.distance_km == 0:
            return 0.0
        return round(self.time_min / self.distance_km, 2)

    def __str__(self) -> str:
        return (
            f"  {self.run_date} | {self.distance_km} km | "
            f"{self.time_min} min | pace {self.pace} min/km"
        )