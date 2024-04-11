'''
787. Cheapest Flights Within K Stops
Medium
Topics
Companies
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 
Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
Example 3:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
'''
from typing import List
from collections import deque, defaultdict
import heapq # as this needs to prioritize the step, better not to use heapq

inf = 1e10

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # adj-list
        edges = defaultdict(list)
        for s, d, price in flights:
            edges[s].append((d, price))

        q = deque([(src, 0)]) # [node, price]: it takes 0 price to reach src
        visited = [inf] * n
        visited[src] = 0
        k += 1

        while k>0 and q:
            size = len(q)
            while size > 0:
                curr, price = q.popleft()
                # for all neighbors
                for node, price_ in edges[curr]:
                    # print(node, price)
                    new_price = price_ + price
                    if new_price < visited[node]:
                        visited[node] = new_price
                        q.append((node, new_price))
                size -= 1
            k -= 1

        return visited[dst] if visited[dst] != inf else -1



if __name__ == "__main__":
    print("743. Network_delay_time.py")

    solution = Solution()
    print("\nCase 1")
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    n = 4
    k = 1
    res = solution.findCheapestPrice(n, flights, src, dst, k)  
    ans = 700
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 2")
    flights = [[0,1,100],[1,2,100],[0,2,500]] 
    src = 0
    dst = 2
    n = 3
    k = 1
    res = solution.findCheapestPrice(n, flights, src, dst, k) 
    ans = 200
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 3")
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    n = 3
    k = 0
    res = solution.findCheapestPrice(n, flights, src, dst, k) 
    ans = 500
    print(res, "\n  ==> check: ", res==ans)
