from agents.folder_agent import FolderAgent


class AgentRegistry:

    def __init__(self):

        self.agents = {}

        self.register(
            "scan_folder",
            FolderAgent(
                "Folder Scanner Agent",
                "C:\\IGRA\\Data"
            )
        )


    def register(self, mission_type, agent):

        self.agents[mission_type] = agent


    def get_agent(self, mission_type):

        return self.agents.get(
            mission_type
        )


    def list_agents(self):

        return list(
            self.agents.keys()
        )