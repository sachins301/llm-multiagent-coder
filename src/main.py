import ast
import json
import re
import sys
from dotenv import load_dotenv
import os
from crewai import Crew, Process
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction


from agents.developer_agent import DeveloperAgent
from agents.lead_agent import LeadAgent
from agents.tester_agent import TesterAgent
from tasks.developer_task import DeveloperTask
from tasks.lead_task import LeadTask
from tasks.test_task import TestTask

def run():
    input_expression = ''
    if sys.stdin.isatty():
        # Running in interactive mode
        while True:
            try:
                input_expression = input("Enter the prompt: ")
                if input_expression.lower() == 'exit':
                    sys.exit(0)  # Exit the program if 'exit' is entered
                break  # Break the loop after getting a valid expression
            except EOFError:
                sys.exit(0)  # Exit the program if EOF is encountered
    else:
        # Running in non-interactive mode (e.g., in CI/CD pipeline)
        print("Running in non-interactive mode. Please provide an expression as a command-line argument.")
        if len(sys.argv) > 1:
            input_expression = sys.argv[1]  # Take the first command-line argument as the expression
        else:
            print("Error: No expression provided.")
            sys.exit(1)  # Exit with an error code if no expression is provided



    lead = LeadAgent().get_agent()
    lead_task = LeadTask().plan(input_expression, lead)

    lead_crew = Crew(
        agents = [lead],
        tasks = [lead_task]
    )

    subtasks = lead_crew.kickoff()
    subtasks = ast.literal_eval(subtasks.raw)
    # print(subtasks)
    dev_tasks = []
    developer = DeveloperAgent().get_agent()
    cleaner = DeveloperAgent().get_cleaner()
    for subtask in subtasks:
        prompt = f"""{subtask['prompt']}, Function name: {subtask['function_name']}"""
        task = DeveloperTask().develop(prompt, developer)
        dev_tasks.append(task)

    # cleaner_task = DeveloperTask().clean(cleaner)
    # number_of_functions = len(dev_tasks)
    dev_crew = Crew(
        agents = [developer],
        tasks = [task for task in dev_tasks],
        process= Process.sequential,
        memory= True,
        verbose= True,
        embedder={
            "provider": "ollama",
            "config": {
                "model": "mxbai-embed-large"
            }
        }
    )

    result = dev_crew.kickoff()

    # Print results
    print("\n\n################################################")
    print("## Here is the result")
    print("################################################\n")
    print(result)


    # Extract all content within triple backticks
    code_blocks = re.findall(r'```([\s\S]*?)```', result.raw)

    # Join all extracted code blocks into a single string
    code = "\n\n".join(code_blocks).strip()

    # Display the cleaned code for verification
    print("\n\n################################################")
    print(code)

    # Write the cleaned code to a file
    with open("generated_code.py", "w") as code_file:
        code_file.write(code)

    ## Tester Crew Implementation
    tester = TesterAgent().get_agent()
    test_tasks = []

    prompt = f"""Developer Code tasks : \n{json.dumps(subtasks)}"""
    task = TestTask().test(prompt, tester)
    test_tasks.append(task)


    testing_crew = Crew(
        agents = [tester],
        tasks = [task for task in test_tasks],
        process= Process.sequential,
        memory= True,
        verbose= True,
        embedder={
            "provider": "ollama",
            "config": {
                "model": "mxbai-embed-large"
            }
        }
    )

    test_result = testing_crew.kickoff()
    # Extract all content within triple backticks
    test_code_blocks = re.findall(r'```([\s\S]*?)```', test_result.raw)

    # Join all extracted code blocks into a single string
    test_code = "\n\n".join(test_code_blocks).strip()

    # Display the cleaned code for verification
    print("\n\n################################################")
    print(test_code)

    # Write the cleaned code to a file
    with open("generated_test_code.py", "w") as code_file:
        code_file.write(test_code)

if __name__ == '__main__':
    load_dotenv()  # Load variables from .env file
    run()