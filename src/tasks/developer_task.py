from crewai import Agent, Task

class DeveloperTask():
    def develop(self, input: str, agent: Agent) -> Task:
        return Task(
            description= f"""Develop a python function to implement the instruction
            input: {input}
            """,
            goal = "Return a python function as per user needs",
            expected_output= "Python code snippet",
            agent = agent
        )