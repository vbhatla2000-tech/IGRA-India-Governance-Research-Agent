from core.mission import Mission
from core.queue import MissionQueue
from core.executor import Executor


mission = Mission(
    "Scan IGRA Data Folder",
    {
        "type": "scan_folder"
    }
)


queue = MissionQueue()

queue.add(mission)


executor = Executor()


task = queue.get_next()


if task:
    executor.execute(task)


print("Mission Completed")