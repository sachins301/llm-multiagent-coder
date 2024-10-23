from crewai import LLM, Agent

class DeveloperAgent():
    def __init__(self) -> None:
        self.llm = LLM(model='ollama/llama3')

    def get_agent(self) -> Agent:
        return Agent(
            role = "Developer",
            goal = "Write a python function to implement the instruction",
            backstory = "You are a developer that returns a python function as per user needs",
            llm = self.llm,
            verbose= True
        )