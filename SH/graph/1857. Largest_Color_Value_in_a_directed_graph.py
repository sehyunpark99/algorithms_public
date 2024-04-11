'''
1857. Largest Color Value in a Directed Graph
Hard
Topics
Companies
Hint
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.
'''

from typing import List
from collections import deque
from collections import defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
        
        # Return max freq of color
        def dfs(node):
            # Detect cycle before visited condition
            if node in path:
                return float("inf") # cycle detected, inf as we are deducing max value
            if node in visit:
                return 0 # immediately 0            
            visit.add(node)
            path.add(node)
            colorIndex = ord(colors[node]) - ord('a') # to map a to 0 and so on (ASCII)
            count[node][colorIndex] == 1 # node it some color and we want to map it to 1 initially

            for w in adj[node]:
                if dfs(w) == float("inf"):
                    return float("inf")
                for col in range(26):
                    count[node][c] = max(count[node][col], (1 if c == colorIndex else 0)+count[w][col]) # find max for specific color
            path.remove(node) # pop path to detect cycle, let visited stay still since we do not want to visit node twice
            return max(count[node]) # give max frequency of color
            

        n, res = len(colors), 0 
        visit, path = set(), set() # to keep track of cycles (which were in call stack) & avoid repeated nodes
        count = [[0] * 26 for i in range(n)] # 2d grid to map count[node][color] -> max freq color // 26 colors
        for i in range(n):
            res = max(dfs(i), res)

        return res if res != float("inf") else -1
    
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        indegrees = [0] * n
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            indegrees[edge[1]] += 1
        zero_indegree = deque()
        for i in range(n):
            if indegrees[i] == 0:
                zero_indegree.append(i)
        counts = [[0]*26 for _ in range(n)]
        for i in range(n):
            counts[i][ord(colors[i]) - ord('a')] += 1
        max_count = 0
        visited = 0
        while zero_indegree:
            u = zero_indegree.popleft()
            visited += 1
            for v in graph[u]:
                for i in range(26):
                    counts[v][i] = max(counts[v][i], counts[u][i] + (ord(colors[v]) - ord('a') == i))
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    zero_indegree.append(v)
            max_count = max(max_count, max(counts[u]))
        return max_count if visited == n else -1