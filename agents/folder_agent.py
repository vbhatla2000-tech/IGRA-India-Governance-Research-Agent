import os
from .base_agent import BaseAgent   # relative import

class FolderAgent(BaseAgent):
    def __init__(self, name: str, path: str):
        super().__init__(name)
        self.path = path

    def run(self):
        print(f"[{self.name}] Scanning folder: {self.path}")
        if os.path.exists(self.path):
            for item in os.listdir(self.path):
                print(" -", item)
        else:
            print("Path does not exist:", self.path)
