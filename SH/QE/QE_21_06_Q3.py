# Consider an adjacency list implementation of an undirected graph using a dictionary. You should implement
# a function LexSmallest(G, u, v) that takes an undirected graph G and two vertices u and v as arguments.
# It returns the lexicographically smallest path between u and v. The list contains the id of the nodes on the
# path (i.e., it is a list of strings). If there is no path between u and v, LexSmalles(G, u, v) returns an
# empty list. For example, consider the following graph G:

# The lexicographic order (also known as dictionary order) is a generalization of the alphabetical order of the
# dictionaries to sequences of ordered symbols. For two lists of strings P1 and P2, P1 is lexicographically smaller
# than P2 if and only if there exists an integer k such that P1[0] = P2[0], P1[1] = P2[1], ..., P1[k-1] =
# P2[k-1], and P1[k] < P2[k]. In the example graph G, the lexicographically smallest path between t and
# v is [‘t’, ‘s’, ‘w’, ‘r’, ‘v’]. The returned list must include every vertex in the lexicographically
# smallest path. Your solution should be based on the Depth-First Search (DFS) algorithm.

class GNode:
    def __init__(self, id, color="W", d=0, f=-1, p=None):
        self.id = id # id is a string
        # "W" = not visited, "G" = visited not all neighbors visited, 
        # "B" = all neighbors also visited
        self.color = color # color (status) of node 
        self.distance = d
        self.finish_time = f
        self.parent = p
    def __str__(self):
        return self.id
    
def LexSmallest(G, source, target):
    paths, targets = [], []

    def dfs(node):
        paths.append(node.id)
        if node == target:
            targets.append(paths[:])
        node.color = "G"
        for w in G.get(node, []):
            if w.color == "W":
                dfs(w)
        node.color == "B"
        paths.pop()

    dfs(source)
    return targets


if __name__ == "__main__":
    print("QE_21_06_Q3.py")
    print("\nCase 1")
    # Example usage:
    r, s, t, u, v = GNode('r'), GNode('s'), GNode('t'), GNode('u'), GNode('v')
    w, x, y = GNode('w'), GNode('x'), GNode('y')
    G = dict()
    G[r], G[w], G[t], G[u] = [w, v], [s, r, t], [s, x, w], [y]
    G[v], G[s], G[x], G[y] = [r], [w, t, x], [s, t], [u]
    
    result = LexSmallest(G, t, v) # ['t', 's', 'w', 'r', 'v']
    print(result)

    print(LexSmallest (G, u, u)) # ['u']
    print(LexSmallest(G, w, y)) # []


# GPT Version  
# def dfs(graph, u, v, path, smallest_path):
#     # Mark the current vertex as visited
#     path.append(u)
    
#     # If the current vertex is the target vertex v
#     if u == v:
#         # Update the smallest path if the current path is lexicographically smaller
#         if len(smallest_path) == 0 or path < smallest_path:
#             smallest_path[:] = path[:]
#         # Backtrack to explore other paths
#         path.pop()
#         return
    
#     # Explore adjacent vertices in lexicographical order
#     for neighbor in sorted(graph[u]):
#         if neighbor not in path:
#             dfs(graph, neighbor, v, path, smallest_path)
    
#     # Backtrack
#     path.pop()

# def LexSmallest(G, u, v):
#     # Check if the vertices exist in the graph
#     if u not in G or v not in G:
#         return []
    
#     # Initialize variables to store the lexicographically smallest path
#     smallest_path = []
#     path = []
    
#     # Perform DFS traversal from vertex u to find the lexicographically smallest path to vertex v
#     dfs(G, u, v, path, smallest_path)
    
#     return smallest_path

# # Example graph G represented as an adjacency list
# G = {
#     's': ['r', 'w'],
#     'r': ['s', 'v'],
#     'w': ['s', 't'],
#     't': ['w', 'x', 'u'],
#     'u': ['t', 'x', 'y'],
#     'v': ['r'],
#     'x': ['t', 'u', 'y'],
#     'y': ['u', 'x']
# }

# # Test the LexSmallest function
# u = 't'
# v = 'v'
# print(LexSmallest(G, u, v))  # Output: ['t', 'w', 's', 'r', 'v']
