# 2360. Longest Cycle in a Graph
# Solved
# Hard
# Topics
# Companies
# Hint
# You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

# The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. 
# If there is no outgoing edge from node i, then edges[i] == -1.

# Return the length of the longest cycle in the graph. If no cycle exists, return -1.

# A cycle is a path that starts and ends at the same node.

import isapi
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


# Invalid
class Solution:
    def longestCycle(self, graph: GNode) -> int:
        count = -1
        history = {} # {0: 0, 3: 1, 2: 2, 4: 3, 1: 0}
        visited = {}
        for key in G.keys():
            visited[key.id] = 0
        print(visited)
        for key in G.keys():
            if visited[key.id] == 0: # if the node has not been visited yet
                queue = set()
                x = key
                l = 0
                while x is not None and visited[x.id] == 0: # if it is connected and not visited
                    visited[x] = 1
                    history[x] = l # is like a path with number of nodes visited
                    l += 1
                    queue.add(x)
                    x = graph.get(x, []) # move on to next edge
                if x!=-1 and x in queue:
                    count = max(count, l-history[x])
        return count


if __name__ == "__main__":
    print("GNode_2360_Longest_Cycle_in_a_Graph.py")

    solution = Solution()
    print("\nCase 1")

    edges_1 = [3,3,4,2,3]
    A, B, C, D, E, F = GNode('A'), GNode('B'), GNode('C'), GNode('D'), GNode('E'), GNode('F')
    G = dict()
    G[A], G[B], G[C], G[D], G[E] = [D], [D], [E], [C], [D]
    print(_show_GNode(G))
    res = solution.longestCycle(G)  # Output: 3
    ans = 3
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 2")
    edges_2 = [2,-1,3,1]
    res = solution.longestCycle(edges_2)  # Output: -1
    ans = -1
    print(res, "\n  ==> check: ", res==ans)


    # Thunder
    # Coloring Algorithm
    # color = [-1] * len(edges)
    # count = -1 # for shortest cycle, it should be INF and need additional condition like ans if ans<INF else -1

