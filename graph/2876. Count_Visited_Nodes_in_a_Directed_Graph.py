from collections import Counter
import collections

class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        degree = Counter(edges)
        visited = set()
        queue = deque()
        # Initial Setting
        for x in range(n): 
            if degree[x] == 0: 
                queue.append(x)
                
        while queue: 
            x = queue.popleft()
            visited.add(x)
            # Go on to the element
            x = edges[x]
            # Initialize
            degree[x] -= 1
            # After going through degree measurements
            if degree[x] == 0: 
                queue.append(x)
        
        ans = [0]*n 
        for x in set(range(n)) - visited: 
            if ans[x] == 0: 
                vals = []
                while not vals or x != vals[0]: 
                    # add on number of connections
                    vals.append(x)
                    x = edges[x]
                for x in vals: 
                    ans[x] = len(vals)
                
        for x in visited: 
            stack = []
            while ans[x] == 0: 
                stack.append(x)
                x = edges[x]
            while stack: 
                ans[stack[-1]] = 1+ans[x]
                x = stack.pop()
        return ans 