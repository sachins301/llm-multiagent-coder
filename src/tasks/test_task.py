from crewai import Agent, Task

class TestTask():
    def test(self, input: str, agent: Agent) -> Task:
        return Task(
            description= f"""Add the testing code in input llm response to the result and append to it the resoponse for the following instruction. 
            Develop a python function to implement test cases for the instruction
            input: {input}
            Add the output to a combined python file along with the previous code snippet if one exists. 
            """,
            goal = "Return a python test function as per user needs",
            expected_output= "Python code snippet",
            agent = agent
        )