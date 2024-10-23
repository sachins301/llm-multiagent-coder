from crewai import LLM, Agent

class LeadAgent:
    def __init__(self) -> None:
        self.llm = LLM(model='ollama/llama3')

    def get_agent(self) -> Agent:
        return Agent(
            role = "Software Development Technical Lead",
            goal = "Breakdown the user instruction into smaller steps",
            backstory = "You are a tech lead that breakdowns the user instruction into smaller individual tasks",
            llm = self.llm,
            verbose= True
        )