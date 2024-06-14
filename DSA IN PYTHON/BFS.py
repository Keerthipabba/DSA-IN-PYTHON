def bfs(graph,start_node):
    visited=set()
    queue=[start_node]
    result=[]
    while queue:
        node=queue.pop(0)
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result
graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}
start_node='A'
print("BFS Traversal starting from node A:")
print(bfs(graph, start_node))