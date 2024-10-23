from crewai import Agent, Task
from src.agents.developer_agent import DeveloperAgent
from src.agents.lead_agent import LeadAgent

class LeadTask:
    def plan(self, input: str, agent: Agent) -> Task:
        return Task(
            description= f"""Split the instruction into smaller tasks. Each task should be a prmpt for the developer to create a python function.
            input: {input}
            """,
            goal = "Split the instruction into smaller steps to be executed in sequence by the developer",
            expected_output= """List of prompts for each function needed for the algorithm. Do not include any other text other than the list.
            Example: [{'function_name': 'function1', 'prompt': 'prompt1'}, {'function_name': 'function2', 'prompt': 'prompt2'}]""",
            agent = agent
        )