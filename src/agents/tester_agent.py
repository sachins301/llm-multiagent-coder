from crewai import LLM, Agent

from tools.code_cleaning_tool import CodeCleaningTool

class TesterAgent():
    def __init__(self) -> None:
        self.llm = LLM(model='ollama/llama3')

    def get_agent(self) -> Agent:
        return Agent(
            role = "Tester",
            goal = "Write test cases for the python function to implement the instruction and combine all the code snippets into a single python file",
            backstory = "You are a tester that returns a python test cases for all the input function description",
            llm = self.llm,
            verbose= True
        )

    def get_cleaner(self) -> Agent:
        return Agent(
            role = "Tester",
            goal = "Clean the input llm response to remove any unwanted text. Output should be a python code snippet that can be executed",
            backstory = "Support developer that cleans the input llm response and returns a python code snippet that can be executed",
            llm = self.llm,
            tools=[CodeCleaningTool()],
            verbose= True
        )
    
    # def run_tests(self, testfile: str, devfile: str) -> Agent:
    #     return Agent(
    #         role = "Tester",
    #         goal = "Run the test cases using the test file and dev file. Depending on the output of test case, make necessary changes in the dev file",
    #         backstory = "You are a teste",
    #         llm = self.llm,
    #         tools=[CodeExecutor(testfile)],
    #         verbose= True
    #     )