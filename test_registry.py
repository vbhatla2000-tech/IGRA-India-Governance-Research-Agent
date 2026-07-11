from core.agent_registry import AgentRegistry


registry = AgentRegistry()


print("Available Agents:")


for agent in registry.list_agents():

    print("-", agent)