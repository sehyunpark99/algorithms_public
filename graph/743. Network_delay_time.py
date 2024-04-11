''''
743. Network Delay Time
Medium
Topics
Companies
Hint
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
'''
from typing import List
from collections import deque, defaultdict

inf = 1e10

# not passed all test cases
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # # Adj_mat construction
        # # row: source, column: destination, element: time
        # graph = [[inf] * n for _ in range(n)]
        # for time in times:
        #     print(time)
        #     graph[time[0]-1][time[1]-1] = time[2]
        
        # Adj-list
        edges = defaultdict(list)
        for s, d, w in times:
            edges[s].append((d, w)) # can be multiple paths
        
        minHeap = deque([(0, k)]) # min time to reach k is 0
        visited = set()
        min_time = 0
        while minHeap:
            w_, n_ = minHeap.popleft()

            if n_ in visited:
                continue

            visited.add(n_)
            min_time = w_

            # for next node
            for n_n, w_n in edges[n_]:
                if n_n not in visited:
                    minHeap.append((w_ + w_n, n_n))


        return min_time if len(visited) == n else -1

# Solution using deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dp = [sys.maxsize] * n
        # need dp to store costs
        dp[k-1] = 0
        graph = defaultdict(list)
        for s, e, w in times:
            graph[s].append((e, w))
            
        dq = deque([k])
        visited = set([k])
        while dq:
            node = dq.popleft()
            cost = dp[node-1]
            visited.remove(node)
            for nei, w in graph[node]:
                if dp[nei-1] > cost + w:
                    dp[nei-1] = cost + w
                    if nei not in visited:
                        visited.add(nei)
                        dq.append(nei)
        
        ans = 0                    
        for i in range(n):
            if i != k-1:
                ans = max(ans, dp[i])
        return ans if ans != sys.maxsize else -1

# import heapq
# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         # Create a defaultdict to store the adjacency list representation of the graph
#         edges = defaultdict(list)
        
#         # Populate the adjacency list with the given edges and weights
#         for u, v, w in times:
#             edges[u].append((v, w))

#         # Initialize a minHeap with (0, k), where k is the starting node and 0 is the distance to k
#         minHeap = [(0, k)]
        
#         # Initialize a set to keep track of visited nodes
#         visit = set()
        
#         # Initialize the time variable to track the maximum time taken to reach all nodes
#         t = 0
        
#         # While there are elements in the minHeap
#         while minHeap:
#             # Pop the node with the minimum distance from the minHeap
#             w1, n1 = heapq.heappop(minHeap)
            
#             # If the node has been visited, continue to the next iteration
#             if n1 in visit:
#                 continue
            
#             # Mark the current node as visited
#             visit.add(n1)
            
#             # Update the time to the current distance
#             t = w1

#             # Iterate over the neighbors of the current node
#             for n2, w2 in edges[n1]:
#                 # If the neighbor has not been visited yet
#                 if n2 not in visit:
#                     # Add the neighbor to the minHeap with updated distance
#                     heapq.heappush(minHeap, (w1 + w2, n2))
        
#         # If all nodes have been visited, return the maximum time taken
#         return t if len(visit) == n else -1

if __name__ == "__main__":
    print("743. Network_delay_time.py")

    solution = Solution()
    print("\nCase 1")

    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    res = solution.networkDelayTime(times, n, k)  # Output:      3
    ans = 2
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 2")
    times = [[1,2,1]]
    n = 2
    k = 1
    res = solution.networkDelayTime(times, n, k)  # Output: -1
    ans = 1
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 3")
    times = [[1,2,1]]
    n = 2
    k = 2
    res = solution.networkDelayTime(times, n, k)  # Output: -1
    ans = -1
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 4")
    times = [[1,2,1],[2,3,2],[1,3,4]]
    n = 3
    k = 1
    res = solution.networkDelayTime(times, n, k)  # Output: -1
    ans = 3
    print(res, "\n  ==> check: ", res==ans)

