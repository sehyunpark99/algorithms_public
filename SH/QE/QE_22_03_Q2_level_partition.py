# BFS Level Partition

class GNode:
    def __init__(self, id, color="W", d=0, p=None):
        self.id = id # id is a string
        # "W" = not visited, "G" = visited not all neighbors visited, 
        # "B" = all neighbors also visited
        self.color = color # color (status) of node 
        self.distance = d
        self.parent = p
    def __str__(self):
        return self.id
    
from collections import deque
# (a) [10 pts] Write a function bfs(G, s) that performs a breadth-first search (BFS) 
# algorithm on a connected undirected graph G from the source node s.
# Version 1
def bfs(G, s):
    q = deque([s]) # for level partitioning, we need depth
    path = []
    while q:
        curr = q.popleft() # pop(0)
        path.append(curr.id)
        # cycle detected
        for w in G.get(curr, []):
            curr.color = "G"
            if w.color == "W":
                w.color = "G"
                w.distance = curr.distance + 1
                w.parent = curr
                q.append(w)
            curr.color = "B"
    return path
# ['r', 's', 't', 'u', 'v', 'w', 'x', 'y', 's', 'v', 'w', 'x', 'u', 'y']    
# sorted(path): ['r', 's', 's', 't', 'u', 'u', 'v', 'v', 'w', 'w', 'x', 'x', 'y', 'y']

# Version 2
# def bfs(G, s):
#     q = deque([(s, 0)]) # for level partitioning, we need depth
#     path = []
#     node_dict = dict()

#     while q:
#         curr, curr_depth = q.popleft()
#         node_dict[curr.id] = curr_depth
#         # cycle detected
#         for w in G.get(curr, []):
#             curr.color = "G"
#             if w.color == "W":
#                 w.color = "G"
#                 w.parent = curr
#                 q.append((w, curr_depth+1))
#             curr.color = "B"
#     return node_dict
# {'s': 0, 'w': 1, 'r': 1, 't': 2, 'x': 2, 'v': 2, 'u': 3, 'y': 3}


# (b) [40 pts] Write the function level partition(G, s) that uses bfs(G, s).
# Version 1
def level_partition(G, s):
    bfs(G, s)
    ans = [[] for _ in range(max(node.distance for node in G.keys())+1)]
    for node in G.keys():
        ans[node.distance].append(node.id)
    return ans
# [['s'], ['r', 'w'], ['t', 'v', 'x'], ['u', 'y']]

# Version 2
# def level_partition(G, s):
#     node_dict = bfs(G, s)
#     max_depth = max(node_dict.values())
#     ans = [[] for _ in range(max_depth+1)]

#     for k, v in node_dict.items():
#         ans[v].append(k)

#     return ans
# [['s'], ['w', 'r'], ['t', 'x', 'v'], ['u', 'y']]


if __name__ == "__main__":
    print("QE_23_03_Q2.py")
    print("\nCase 1")
    # Example usage:
    r, s, t, u, v = GNode('r'), GNode('s'), GNode('t'), GNode('u'), GNode('v')
    w, x, y = GNode('w'), GNode('x'), GNode('y')
    G = dict()
    G[r], G[s], G[t], G[u], G[v] = [s, v], [w, r], [w, x, u], [t, x, y], [r]
    G[w], G[x], G[y] = [s, t, x], [w, t, u, y], [x, u]
    print(bfs(G, s))
    result = level_partition(G, s) # Output: [['s'], ['w', 'r'], ['t', 'x', 'v'], ['u', 'y']]
    print(result)


# DFS
# from collections import deque
# from typing import List

# class GNode:
#     def __init__(self, id, color="W", d=0, p=None):
#         self.id = id
#         self.color = color
#         self.distance = d
#         self.parent = p

# def dfs(G, s):
#     stack = [s]
#     path = []
#     while stack:
#         curr = stack.pop()  # pop the last node
#         path.append(curr.id)
#         for w in G.get(curr, []):
#             if w.color == "W":
#                 w.color = "G"
#                 w.distance = curr.distance + 1
#                 w.parent = curr
#                 stack.append(w)
#         curr.color = "B"
#     return path

# def level_partition(G, s):
#     dfs(G, s)
#     max_depth = max(node.distance for node in G.keys())
#     ans = [[] for _ in range(max_depth + 1)]
#     for node in G.keys():
#         ans[node.distance].append(node.id)
#     return ans

# if __name__ == "__main__":
#     print("QE_23_03_Q2.py")
#     print("\nCase 1")
#     r, s, t, u, v = GNode('r'), GNode('s'), GNode('t'), GNode('u'), GNode('v')
#     w, x, y = GNode('w'), GNode('x'), GNode('y')
#     G = dict()
#     G[r], G[s], G[t], G[u], G[v] = [s, v], [w, r], [w, x, u], [t, x, y], [r]
#     G[w], G[x], G[y] = [s, t, x], [w, t, u, y], [x, u]
#     print(dfs(G, s))
#     result = level_partition(G, s) 
#     print(result)  # Output: [['s'], ['w', 'r'], ['t', 'x', 'v'], ['u', 'y']]
