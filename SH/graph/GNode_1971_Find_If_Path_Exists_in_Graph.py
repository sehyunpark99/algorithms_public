from GNode_by_Thunder import _show_GNode
from collections import defaultdict, deque
from typing import List

class GNode:
    def __init__(self, id, color="W", p=None):
        '''
        [color spec]
        W: not visited
        G: visited but its neighbors are not visited 
        B: visited and all the neighbors are visited 
        '''
        self.id = id # str
        self.color = color # act as a visited list
        self.parent = p

    def __str__(self):
        return str(self.id)

    def __hash__(self):
        return hash(self.id)

    def reset(self):
        self.color = "W"
        self.parent = None

    def dfs(self):
        if self.color == "W":
            print("Visiting node:", self.id)
            self.color = "G"
            for neighbor in self.neighbors:
                neighbor.dfs()
            self.color = "B"

    def bfs(self):
        queue = deque([self])

        while queue:
            node = queue.popleft()
            if node.color == "W":
                print("Visiting node:", node.id)
                node.color = "G"
                for neighbor in node.neighbors:
                    if neighbor.color == "W":
                        queue.append(neighbor)
                node.color = "B"

# BFS
def validPath_bfs(graph: GNode, source: GNode, destination: int) -> bool:
    # Queue for BFS -> Should start from source (=root)
    queue = deque()
    queue.append(source)
    visit = {}
    while queue:
        curr = queue.popleft()
        if curr == destination:
            return True
        # If this node has been visited -> No need to 
        if curr.color == "B":
            continue
        # Mark the node as visited
        curr.color= "G"
        # For all adjacent nodes
        for v in graph.get(curr, []):
            if v == destination:
                return True
            elif v.color == "W":
                queue.append(v)
        curr.color = "B"
    return False   

# DFS
def validPath_dfs(graph: GNode, source: GNode, destination: int) -> bool:
    visited = set()
    def dfs(node):
        # Base Case
        if node == destination:
            return True
        node.color = "G"
        for w in graph.get(node, []):
            if w.color == "W":
                if dfs(w):
                    return True
        node.color == "B"
        return False
    return dfs(source)


if __name__ == "__main__":
    print("GNode_1971_Find_if_path_exists_in_graph.py")
    print("\nCase 1")
    # Example usage:
    n = 6
    edges = [['A','B'],['A','C'],['D','F'],['F','E'],['E','D']]
    A, B, C, D, E, F = GNode('A'), GNode('B'), GNode('C'), GNode('D'), GNode('E'), GNode('F')
    source = A
    destination = C
    G = dict()
    G[A], G[D], G[F], G[E] = [B, C] , [F], [E], [D]


    print(_show_GNode(G))
    print(validPath_dfs(G, source, destination)) # True
    print(validPath_bfs(G, source, destination)) # True


# Original Answers
# Adjacency Matrix with DFS
# def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#     graph = [[] for _ in range(n)]
#     # Matrix construction
#     for edge in edges:
#         graph[edge[0]].append(edge[1])
#         graph[edge[1]].append(edge[0])
#     # dfs
#     visited = set()
#     def dfs(node):
#         # Base Case
#         if node == destination:
#             return True
#         visited.add(node)
#         for w in graph[node]:
#             if w not in visited:
#                 if dfs(w):
#                     return True
#         return False
#     return dfs(source)
    
# BFS
# def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#     # adj_list = {i:[] for i in range(n)}
#     graph = defaultdict(list)
#     for v1,v2 in edges:
#         graph[v1].append(v2)
#         graph[v2].append(v1)
        
#     # Queue for BFS -> Should start from source (=root)
#     queue = deque()
#     queue.append(source)
#     visit = [0]*n
#     while queue:
#         curr = queue.popleft()
#         if curr == destination:
#             return True
#         # If this node has been visited -> No need to 
#         if visit[curr]:
#             continue
#         # Mark the node as visited
#         visit[curr] = True
#         # For all adjacent nodes
#         for v in graph[curr]:
#             if v == destination:
#                 return True
#             elif not visit[v]:
#                 queue.append(v)
#     return False   