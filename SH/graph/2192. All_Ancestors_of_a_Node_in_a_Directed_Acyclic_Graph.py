'''
2192. All Ancestors of a Node in a Directed Acyclic Graph
Medium
Topics
Companies
Hint
You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.

Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

A node u is an ancestor of another node v if u can reach v via a set of edges.
'''
from typing import List
from collections import defaultdict, deque

# BFS
# 
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Directed Graph
        graph = defaultdict(list) # {0: [1, 2, 3, 4], 1: [2, 3, 4], 2: [3, 4], 3: [4]}
        for edge in edges:
            graph[edge[0]].append(edge[1])

        ans = [[] for _ in range(n)] # lists for all nodes
        
        q = deque(graph)
        path = []
        while q:
            curr = q.popleft() # only the source pops off
            path.append(curr)
            for w in graph[curr]:
                if curr not in ans[w]:
                    ans[w].append(curr)
                    q.append(w)
                for elem in ans[curr]:
                    if elem not in ans[w]:
                        ans[w].append(elem)

        ans = [(sorted(list(s))) for s in ans]
        return ans

# BFS: in_degree
# class Solution:
#     def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
#         #Use Kahn's algorithm of toposort using a queue and bfs!
#         graph = [[] for _ in range(n)]
#         indegrees = [0] * n
        
#         #Time: O(n^2)
#         #Space: O(n^2 + n + n) -> O(n^2)
        
#         #1st step: build adjacency list grpah and update the initial indegrees of every node!
#         for edge in edges:
#             src, dest = edge[0], edge[1]
#             graph[src].append(dest)
#             indegrees[dest] += 1
        
        
#         queue = deque()
#         ans = [set() for _ in range(n)]
#         #2nd step: go through the indegrees array and add to queue for any node that has no ancestor!
#         for i in range(len(indegrees)):
#             if(indegrees[i] == 0):
#                 queue.append(i)
        
#         #Kahn's algorithm initiation!
#         #while loop will run for each and every node in graph!
#         #in worst case, adjacency list for one particular node may contain all other vertices!
#         while queue:
#             cur = queue.pop()
            
#             #for each neighbor
#             for neighbor in graph[cur]:
#                 #current node is ancestor to each and every neighboring node!
#                 ans[neighbor].add(cur)
#                 #every ancestor of current node is also an ancestor to the neighboring node!
#                 ans[neighbor].update(ans[cur])
#                 indegrees[neighbor] -= 1
#                 if(indegrees[neighbor] == 0):
#                     queue.append(neighbor)
        
#         #at the end, we should have set of ancestors for each and every node!
#         #in worst case, set s for ith node could have all other vertices be ancestor to node i !
#         ans = [(sorted(list(s))) for s in ans]
#         return ans

# DFS
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Directed Graph
        graph = defaultdict(list) # {0: [1, 2, 3, 4], 1: [2, 3, 4], 2: [3, 4], 3: [4]}
        for edge in edges:
            graph[edge[0]].append(edge[1])
        ans = [[] for _ in range(n)] # lists for all nodes
        
        def dfs(ancestor: int, kid: int) -> None:
            if not (ans[kid] and ans[kid][-1] == ancestor):
                if kid != ancestor:
                    ans[kid].append(ancestor)
                for grand_child in graph[kid]:
                    dfs(ancestor, grand_child)
            
        for i in range(n):
            dfs(i, i)
        return ans

# from collections import defaultdict
# from typing import Iterable, List

# class Solution:
#     def getAncestors(self, n: int, edges: List[List[int]]) -> Iterable[List[int]]:
#         def dfs(u: int) -> set:
#             if not ancestors[u]:
#                 for v in graph[u]:
#                     if v not in ancestors[u]:
#                         ancestors[u].update({v} | dfs(v))
#             return ancestors[u]

#         graph = defaultdict(set)
#         for u, v in edges:
#             graph[v].add(u)

#         ancestors = [set() for _ in range(n)]
#         for u in range(n):
#             if not ancestors[u]:
#                 dfs(u)

#         return map(sorted, ancestors)

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        ans = [[] for _ in range(n)]

        g = defaultdict(list)

        for u, v in edges:
            g[v].append(u)
        
        def dfs(node, curr):
            for v in g[curr]:
                if v not in ans[node]:
                    dfs(node, v)
                    ans[node].append(v)  
        
        for i in range(n):
            dfs(i,i)

        for k in ans:
            k.sort()
            
        return ans 


if __name__ == "__main__":
    print("2192. All Ancestors of a Node in a Directed Acyclic Graph.py")

    solution = Solution()
    print("\nCase 1")
    n = 8
    edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
    res = solution.getAncestors(n, edgeList)  
    ans = [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 2")
    n = 5
    edgeList = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    res = solution.getAncestors(n, edgeList)
    ans = [[],[0],[0,1],[0,1,2],[0,1,2,3]]
    print(res, "\n  ==> check: ", res==ans)