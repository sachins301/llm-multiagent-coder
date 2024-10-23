import ast
import sys
from crewai import Crew

from agents.developer_agent import DeveloperAgent
from agents.lead_agent import LeadAgent
from tasks.developer_task import DeveloperTask
from tasks.lead_task import LeadTask

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
    for subtask in subtasks:
        prompt = f"""{subtask['prompt']}, Function name: {subtask['function_name']}"""
        task = DeveloperTask().develop(prompt, developer)
        dev_tasks.append(task)

    dev_crew = Crew(
        agents = [developer],
        tasks = [task for task in dev_tasks]
    )

    result = dev_crew.kickoff()

    # Print results
    print("\n\n################################################")
    print("## Here is the result")
    print("################################################\n")
    print(result)

if __name__ == '__main__':
    run()