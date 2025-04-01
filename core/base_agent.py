class ResearchAgent:
    def __init__(self, name: str, role: str, experience_level: int):
        self.name = name
        self.role = role
        self.experience_level = experience_level

    def report_status(self) -> str:
        return f"{self.name} ({self.role}) is ready to contribute!" 
