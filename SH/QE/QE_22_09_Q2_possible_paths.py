# In this problem, given an acyclic directed graph G, you will implement funciton paths(G, s, t)
# that returns the list of all paths between two certices s and t. A path between two vertices is also a list
# of vertices. Paths in the list can be in any order, and each element in the path (element in the inner list)
# should be the id (string) of the vertex. For example, for the following graph G, paths (G, a, c) returns
# the following list of paths: [["a", "c"], ["a", "b", "d", "c"]]

from typing import List

class GNode:
    def __init__(self, id, color="W", p=None):
        # "W" = not visited, "G" = visited not all neighbors visited, 
        # "B" = all neighbors also visited
        self.id = id # id is a string
        self.color = color # color (status) of node
        self.parent = p

    def __str__(self):
        return self.id
    
# BFS
# This problem works with BFS as it requires to search all the possible paths
# as well as its path in order
def paths(G: GNode, s, t) -> List[List]:
    paths, targets = [[s]], []
    while paths:
        path = paths.pop(0) # since we are using list
        edges = G[path[-1]]
        if not edges:
            continue
        for edge in edges:
            if edge == t:
                tmp = []
                for v in path:
                    tmp.append(v.id)
                
                targets.append(tmp+[edge.id])
            else:
                paths = [path+[edge]] + paths
    return targets


# DFS
def paths(G: GNode, s, t) -> List[List]:
    paths, targets = [], []

    def dfs(node):
        paths.append(node.id)
        if node == t:
            targets.append(paths[:])
        for w in G.get(node, []): # if G[node] does not exist, return []
            dfs(w)
        paths.pop() # get rid of current node 
    dfs(s)
    return targets



if __name__ == "__main__":
    print("QE_22_09_Q2.py")
    print("\nCase 1")
    # Example usage:
    a, b, c, d = GNode('a'), GNode('b'), GNode('c'), GNode('d')
    G = dict()
    G[a], G[b], G[c], G[d] = [b,c], [d], [], [c]
    result = paths(G, a, c) # Output: [["a", "c"], ["a", "b", "d", "c"]]
    print(result)

    # print("\nCase 2")
    # A, B, C = GNode('A'), GNode('B'), GNode('C')
    # D, E, F = GNode('D'), GNode('E'), GNode('F')
    # G = dict()
    # G[A], G[B], G[C] = [D], [E], [B, D]
    # G[F] = []
    # G[D], G[E] = [F], [F]
    # result = paths(G) # Output: []
    # print(result)