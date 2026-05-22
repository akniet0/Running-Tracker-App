class Goal:
    def __init__(self, target_km: float, deadline: str):
        self.target_km = target_km
        self.deadline = deadline

    def is_achieved(self, total_km: float) -> bool:
        return total_km >= self.target_km