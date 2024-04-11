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

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        # Graph Construction
        # defaultdict(<class 'list'>, {0: [3], 1: [3], 2: [4], 3: [2], 4: [3]})
        graph = defaultdict(list)
        for v, w in enumerate(edges):
            graph[v].append(w)

        count = -1
        history = {} # {0: 0, 3: 1, 2: 2, 4: 3, 1: 0}
        visited = [0] * len(edges)
        for i in range(len(edges)):
            if visited[i] == 0: # if the node has not been visited yet
                queue = set()
                x = i
                l = 0
                while x != -1 and visited[x] == 0: # if it is connected and not visited
                    visited[x] = 1
                    history[x] = l # is like a path with number of nodes visited
                    l += 1
                    queue.add(x)
                    x = edges[x] # move on to next edge
                if x!=-1 and x in queue:
                    count = max(count, l-history[x])
        return count

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        indegree = [0] * n
        graph = defaultdict(list)

        for u, v in enumerate(edges):
            if v == -1: continue
            graph[u].append(v)
            indegree[v] += 1

        queue = deque([node for node, indeg in enumerate(indegree) if indeg == 0])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                edges[node] = -1

                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
        
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v in enumerate(edges):
            if v == -1: continue
            pu, pv = find(u), find(v)
            if pu == pv: continue
            if rank[pu] <= rank[pv]:
                parent[pv] = pu
                rank[pu] += rank[pv]
            else:
                parent[pu] = pv
                rank[pv] += rank[pu]
        mx = max(rank)
        return mx if mx != 1 else -1

        
if __name__ == "__main__":
    print("GNode_2360_Longest_Cycle_in_a_Graph.py")

    solution = Solution()
    print("\nCase 1")

    edges_1 = [3,3,4,2,3]
    res = solution.longestCycle(edges_1)  # Output: 3
    ans = 3
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 2")
    edges_2 = [2,-1,3,1]
    res = solution.longestCycle(edges_2)  # Output: -1
    ans = -1
    print(res, "\n  ==> check: ", res==ans)


    # Thunder
    # A, B, C, D, E, F = GNode('A'), GNode('B'), GNode('C'), GNode('D'), GNode('E'), GNode('F')
    # source = A
    # destination = C
    # G = dict()
    # G[A], G[D], G[F], G[E] = [B, C] , [F], [E], [D]

    # print("\nCase 2")
    # 
    # Coloring Algorithm
    # color = [-1] * len(edges)
    # count = -1 # for shortest cycle, it should be INF and need additional condition like ans if ans<INF else -1

    # print(_show_GNode(G))
    # print(validPath_dfs(G, source, destination)) # True
    # print(validPath_bfs(G, source, destination)) # True
