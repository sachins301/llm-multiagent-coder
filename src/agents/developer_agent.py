from crewai import LLM, Agent

from tools.code_cleaning_tool import CodeCleaningTool

class DeveloperAgent():
    def __init__(self) -> None:
        self.llm = LLM(model='ollama/llama3')

    def get_agent(self) -> Agent:
        return Agent(
            role = "Developer",
            goal = "Write a python function to implement the instruction and combine all the code snippets into a single python file",
            backstory = "You are a developer that returns a python function as per user needs",
            llm = self.llm,
            verbose= True
        )

    def get_cleaner(self) -> Agent:
        return Agent(
            role = "Developer",
            goal = "Clean the input llm response to remove any unwanted text. Output should be a python code snippet that can be executed",
            backstory = "Support developer that cleans the input llm response and returns a python code snippet that can be executed",
            llm = self.llm,
            tools=[CodeCleaningTool()],
            verbose= True
        )