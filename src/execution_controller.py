import re
import sys
import os

from crewai import Crew, Process

from agents.developer_agent import DeveloperAgent
from tasks.developer_task import DeveloperTask
from tools.code_executor import CodeExecutor


class ExecutionController:
    def __init__(self):
        pass

    def _run(dev_code_file, test_code_file) -> str:
        exec_status = CodeExecutor._run(test_code_file)
        print("Starting exec status : ", exec_status)
        dev_code = ""
        with open(dev_code_file, 'r') as file:
            dev_code = file.read()

        print("Dev code read : ", dev_code)

        trial_count = 0

        while exec_status != "Success" and trial_count < 3:
            trial_count += 1
            dev_agent = DeveloperAgent().get_agent()
            debug_task = DeveloperTask().debug(dev_code, exec_status, dev_agent)
            debug_crew = Crew(
                agents = [dev_agent],
                tasks = [debug_task],
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
            
            result = debug_crew.kickoff()

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

            exec_status = CodeExecutor._run(test_code_file)
    

if __name__ == '__main__':
    # Path to the generated Python code file
    test_code_file_path = "generated_test_code.py" 
    dev_code_file_path = "generated_code.py"
    result = ExecutionController._run(dev_code_file=dev_code_file_path, test_code_file=test_code_file_path)
    print(result)
