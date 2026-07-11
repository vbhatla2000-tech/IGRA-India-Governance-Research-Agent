class MissionQueue:

    def __init__(self):
        self.tasks = []


    def add(self, mission):
        self.tasks.append(mission)


    def get_next(self):

        if self.tasks:
            return self.tasks.pop(0)

        return None


    def size(self):
        return len(self.tasks)