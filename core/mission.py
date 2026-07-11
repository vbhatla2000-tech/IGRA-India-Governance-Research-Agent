import datetime

class Mission:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.created_at = datetime.datetime.now()
        self.status = "PENDING"

    def start(self):
        self.status = "RUNNING"
        print(f"[{self.name}] Mission started at {self.created_at}")
        print("Description:", self.description)

    def complete(self):
        self.status = "COMPLETED"
        print(f"[{self.name}] Mission completed at {datetime.datetime.now()}")

    def fail(self, reason: str):
        self.status = "FAILED"
        print(f"[{self.name}] Mission failed: {reason}")
