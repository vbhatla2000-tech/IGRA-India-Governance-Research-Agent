from agents.folder_agent import FolderAgent


class Executor:

    def __init__(self):
        self.folder_agent = FolderAgent(
            "Folder Scanner Agent",
            "C:\\IGRA\\Data"
        )


    def execute(self, mission):

        print("DEBUG Mission Object:", mission.__dict__)

        print(
            "Executing mission:",
            mission.name
        )

        action = mission.description["type"]

        if action == "scan_folder":

            self.folder_agent.run()

            mission.status = "COMPLETED"

            return True


        print(
            "Unknown action:",
            action
        )

        mission.status = "FAILED"

        return False