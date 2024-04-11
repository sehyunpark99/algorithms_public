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
def isBipartite(graph: GNode) -> bool:
    def bfs(graph, node):
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            # For all adjacent nodes
            for v in graph.get(curr, []):
                if v.color == "W":
                    if curr.color == "G":
                        v.color = "B"
                    else:
                        v.color = "G"
                    queue.append(v)
                else:
                    if v.color == curr.color:
                        return False
    for node, edges in graph.items():
        if node.color == "W":
            if bfs(graph, node) == False:
                return False        
    return True


if __name__ == "__main__":
    print("GNode_785_Find_if_path_exists_in_graph.py")
    print("\nCase 1")
    # Example usage:
    edges = [[1,2,3],[0,2],[0,1,3],[0,2]]
    A, B, C, D, E, F = GNode('A'), GNode('B'), GNode('C'), GNode('D'), GNode('E'), GNode('F')
    G = dict()
    G[A], G[B], G[C], G[D] =  [B, C, D],[A, C],[A, B, D],[A, C]


    print(_show_GNode(G))
    print(isBipartite(G)) # True
    # print(isBipartite(edges)) # True
