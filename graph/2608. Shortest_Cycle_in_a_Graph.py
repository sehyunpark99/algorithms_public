'''
2608. Shortest Cycle in a Graph
Attempted
Hard
Topics
Companies
Hint
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1. The edges in the graph are represented by a given 2D integer array edges, where edges[i] = [ui, vi] denotes an edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

Return the length of the shortest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node, and each edge in the path is used only once.
'''

from GNode_by_Thunder import _show_GNode
from collections import defaultdict, deque
from typing import List
inf = 1e10

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

def _bfs(G: dict, s: GNode):
    queue = [s]
    path = []
    s.color = "G"

    while queue:
        node = queue.pop(0)
        # print(node.id)
        path.append(node.id)

        for neigh in G[node]:
            if neigh.color == "W":
                neigh.color = "G"
                neigh.parent = node
                queue.append(neigh)
        node.color = "B"
    return sorted(path)

def _bfs_reset(G: dict):
    for node in G.keys():
        node.color = "W"
        node.parent = None
    return None


# BFS
# not working for some test cases
def shotestCycle(edges: List[List[int]]) -> int:
    n = len(edges)
    ans = inf
    # graph = [[] for _ in range(n)]
    # Adjacency Matrix
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    for curr in range(n):
        dist = {}
        # queue: (current node, parent, distance)
        q = deque([(curr, -1, 0)])
        while q:
            curr, p, d = q.popleft()
            if curr in dist:
                ans = min(ans, d+dist[curr])
                break
            dist[curr] = d
            for w in graph[curr]:
                if w != p:
                    q.append((w, curr, d+1))
    return ans if ans < inf else -1

# couldn't cover all the test cases as it assumes one by one match
def findShortestCycle(n: int, edges: List[List[int]]) -> int:
        # Graph Construction
        graph = defaultdict(int)
        for u, v in edges:
            graph[u] = v

        count = inf
        history = {}
        visited = [0] * n
        for i in range(n):
            if visited[i] == 0: # if the node has not been visited yet
                queue = set()
                x = i
                l = 0
                while x != -1 and visited[x] == 0: # if it is connected and not visited
                    visited[x] = 1
                    history[x] = l # is like a path with number of nodes visited
                    l += 1
                    queue.add(x)
                    x = graph[x] # move on to next edge
                if x!=-1 and x in queue:
                    count = min(count, l-history[x])
        return count if count < inf else -1


if __name__ == "__main__":
    print("2608. Shortest Cycle in a Graph.py")
    print("\nCase 1")
    # Example usage:
    n = 7
    edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
    A, B, C, D, E, F, H = GNode('A'), GNode('B'), GNode('C'), GNode('D'), GNode('E'), GNode('F'), GNode('H')
    G = dict()
    G[A], G[B], G[C], G[D], G[E], G[F], G[H] = [B], [C], [A], [E], [F], [H], [C]
    G_2 = dict()
    G_2[A] = [B, C]

    print(_show_GNode(G))
    print(shotestCycle(edges)) # 3
    result_2 = findShortestCycle(n, edges)
    print(result_2)  # Output: 3

'''
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(start):
            # return shortest cycle staring at start
            # store (cur, parent)
            dq = deque([(start, -1)])
            dist = [float('inf')] * n
            dist[start] = 0
            cur_min = float('inf')
            while dq:
                cur, par = dq.popleft()
                for nei in graph[cur]:
                    if dist[nei] == float('inf'):
                        dist[nei] = dist[cur] + 1
                        dq.append((nei, cur))
                    elif nei != par:
                        cur_min = min(cur_min, dist[nei] + dist[cur] + 1)
                # if not comment out below 2 lines and return early, it will fail the list test case, why?? 
                # I thought as long as it finds a cycle, it must be the shortest from this node due to bfs property?
                # if cur_min < float('inf'):
                #     return cur_min
            return cur_min
        
        ans = min([dfs(i) for i in range(n)])
        return ans if ans < float('inf') else -1


    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        shortest = inf
        for i in range(n):
            dq, dist, parent = deque([i]), [inf] * n, [-1] * n
            dist[i] = 0
            while dq:
                node = dq.popleft()
                for kid in g.get(node, set()):
                    if dist[kid] == inf:
                        dist[kid] = dist[node] + 1
                        parent[kid] = node
                        dq.append(kid)
                    elif parent[kid] != node and parent[node] != kid:
                        shortest = min(shortest, dist[node] + dist[kid] + 1)
        return -1 if shortest == inf else shortest                
'''