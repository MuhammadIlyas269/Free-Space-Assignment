"""
BFS Code is copy from below site beacuse actual assigment is to identify data structure for task execution which is graph data structure
Comments with "New" are task execution logic which I own it not copy from any site 
https://www.educative.io/answers/graphs-basics-representation-traversals-and-applications

Assingment Questions:
1. Identify data structure to represent a task?
    Graph Data Structure
2. Assumaption for completion?
    Yes if strongly connected.
3. Unit Test Cases
    
"""
def bfs(graph, start):
    path = []
    queue = [start]
    executed = [] # New
    while queue:
        vertex = queue.pop(0)
        if vertex not in path:
            path.append(vertex)

            # New
            if not graph[vertex]:
                scheduler([vertex])
                executed.append(vertex)
            # New
            
            queue.extend(graph[vertex])
    
    # New
    for i in path[::-1]:
        if i not in executed:
            scheduler([i])
            executed.append(i)
    # New

    return path



test_graph_1 = {
    'Task1': ['Task2'],
    'Task2': ['Task3','Task4'],
    'Task3': ['Task6'],
    'Task4': ['Task1','Task3','Task6'],
    'Task5': [],
    'Task6': ['Task5']
}

test_graph_2 = {
    'Task1': ['Task2'],
    'Task2': ['Task4','Task5'],
    'Task3': [],
    'Task4': ['Task3'],
    'Task5': []
}

def scheduler(tasks):
    for task in tasks:
        execute(task)

def execute(task):
    print(f"Task: {task} is executed successfully")

print('\r')
print("Graph 1 Task Execution")
print("Graph 1 Traversal: ",bfs(test_graph_1, 'Task1'))
print('\r')
print("Graph 2 Task Execution")
print("Graph 2 Traversal: ",bfs(test_graph_2, 'Task1'))
