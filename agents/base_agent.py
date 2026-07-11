from datetime import datetime


class BaseAgent:

    def __init__(self, name):
        self.name = name


    def log(self, message):

        print(
            f"[{datetime.now()}]"
            f"[{self.name}]"
            f"{message}"
        )


    def run(self, task):
        raise NotImplementedError 
