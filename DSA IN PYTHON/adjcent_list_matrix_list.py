def print_adj_list(graph):
    print("Adjacency List:")
    for node, neighbors in enumerate(graph):
        print(f"{node}: {', '.join(map(str, neighbors))}")

def print_adj_matrix(matrix):
    print("Adjacency Matrix:")
    for row in matrix:
       print(" ".join(map(str, row)))

adj_list = [
    [1, 2],
    [2],
    [0, 3],
    [3]
]

num_nodes = 4
adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]
edges = [
    (0, 1), (0, 2),
    (1, 2),
    (2, 0), (2, 3),
    (3, 3)
]

for src, dest in edges:
    adj_matrix[src][dest] = 1

print_adj_list(adj_list)

print_adj_matrix(adj_matrix)