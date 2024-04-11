'''
1557. Minimum Number of Vertices to Reach All Nodes
Medium
Topics
Companies
Hint
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.
'''

from typing import List
from collections import defaultdict, deque

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

# class Solution:
#     def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
#         graph = defaultdict(list)
#         for edge in edges:
#             graph[edge[0]].append(edge[1]) # {0: [1, 2], 2: [5], 3: [4], 4: [2]})

#         visited = []
#         ans = []
#         def dfs(node):
#             if node not in visited:
#                 visited.append(node)
#                 print(visited)
#                 for w in graph[node]:
#                     if w not in visited:
#                         dfs(w)
        
#         start = graph.keys()
#         for nodes in start:
#             if nodes in visited:
#                 continue
#             print("graph keys:", nodes)
#             if nodes not in visited:
#                 dfs(nodes)
#                 ans.append(nodes)
#                 print(ans)

#         return ans


# from collections import defaultdict
# from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1]) # {0: [1, 2], 2: [5], 3: [4], 4: [2]})

        visited = [0] * n
        ans = set()

        def dfs(node):
            visited[node] = 1
            for w in graph[node]:
                if visited[w] == 0:
                    dfs(w)
                elif w in ans:
                    ans.remove(w)
        
        for i in range(n):
            print("graph keys:", i)
            if visited[i] == 0:
                dfs(i)
                ans.add(i)
                # print(ans)

        return list(ans)

# class Solution:
#     def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
#         ans = set(range(n))
#         for e in edges:
#             if e[1] in ans:
#                 ans.remove(e[1])
#         return list(ans)

# class Solution:
#     def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
#         all_nodes = set([i for i in range(n)])
#         reachable = set()

#         for edge in edges:
#             reachable.add(edge[1])

#         return all_nodes - reachable


if __name__ == "__main__":
    print("1557. Minimum Number of Vertices to Reach All Nodes.py")

    solution = Solution()
    print("\nCase 1")
    edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
    n = 6
    res = solution.findSmallestSetOfVertices(n, edges) 
    ans = [0,3]
    print(res, "\n  ==> check: ", res==ans)


    print("\nCase 2")
    n = 5
    edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
    res = solution.findSmallestSetOfVertices(n, edges) 
    ans = [0,2,3]
    print(res, "\n  ==> check: ", res==ans)

