from crewai import Agent, Task

class DeveloperTask():
    def develop(self, input: str, agent: Agent) -> Task:
        return Task(
            description= f"""Add the code in input llm response to the result and append to it the resoponse for the following instruction. 
            Develop a python function to implement the instruction
            input: {input}
            Add the output to a combined python file along with the previous code snippet if one exists. 
            """,
            goal = "Return a python function as per user needs",
            expected_output= "Python code snippet",
            agent = agent
        )
    
    def debug(self, dev_code: str, error_msg: str, agent: Agent) -> Task:
        return Task(
            description= f"""
                Dev Code:
                {dev_code}
                \n
                Error Message:
                {error_msg}

                Modify the dev code to fix the error. 
            """,
            goal = "Return modified python code",
            expected_output= "Python code snippet",
            agent= agent
        )
    
    def clean(self, agent: Agent) -> Task:
        return Task(
            description= """DO NOT INCLUDE ANY TEXT OTHER THAN THE CODE SNIPPET. Clean the input llm response to remove any unwanted text. Output should be a python code snippet that can be executed
            Example:
                LLM Response: ```
import heapq

def find_shortest_path(start_node, end_node, graph):
    # Create a distance dictionary to store the shortest distance from the start node to each node
    distance_dict = {node: float('inf') for edge in graph for node in [edge[1]] if node not in distance_dict}
    distance_dict[start_node] = 0

    # Create a priority queue to hold nodes to be processed, with their distances as priorities
    pq = [(0, start_node)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == end_node:
            break

        for neighbor, edge_weight in get_neighbors(current_node, graph):
            new_distance = current_distance + edge_weight
            if new_distance < distance_dict[neighbor]:
                distance_dict[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    # Build the shortest path by backtracking from the end node to the start node
    path = []
    current_node = end_node
    while current_node != start_node:
        for edge in graph:
            if edge[1] == current_node:
                path.append((current_node, edge[2], edge[0]))
                current_node = edge[0]
                break

    # Return the shortest path and its total distance
    return list(reversed(path)), distance_dict[end_node]
```
This is the output I am expected to provide.

                Output: 
                import heapq

def find_shortest_path(start_node, end_node, graph):
    distance_dict = {node: float('inf') for edge in graph for node in [edge[1]] if node not in distance_dict}
    distance_dict[start_node] = 0
    pq = [(0, start_node)]
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_node == end_node:
            break
        for neighbor, edge_weight in get_neighbors(current_node, graph):
            new_distance = current_distance + edge_weight
            if new_distance < distance_dict[neighbor]:
                distance_dict[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))
    path = []
    current_node = end_node
    while current_node != start_node:
        for edge in graph:
            if edge[1] == current_node:
                path.append((current_node, edge[2], edge[0]))
                current_node = edge[0]
                break
    return list(reversed(path)), distance_dict[end_node]
            
            """,
            goal = "Clean the input llm response to remove any unwanted text. Output should be a python code snippet that can be executed",
            expected_output= "Python code snippet",
            agent = agent
        )