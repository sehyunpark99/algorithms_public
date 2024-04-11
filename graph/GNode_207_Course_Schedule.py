from GNode_by_Thunder import _show_GNode
import collections
from collections import deque
from typing import List

class GNode:
    def __init__(self, id, color="W", p=None):
        '''
        [color spec]
        W: not visited
        G: visited but its neighbors are not visited 
        B: visited and all the neighbors are visited 
        '''
        self.id = id
        self.color = color
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

# DFS
# Case 1
# {'B': ['A'], 'C': ['A'], 'D': ['B', 'C']}
# True

def canFinish(graph)->bool:
    def dfs(node):
        if node.color == "W":
            node.color = "G"
            for neighbor in graph.get(node, []):
                dfs(neighbor)
            node.color = "B"

    # Perform DFS to detect cyclic dependencies
    for node in graph.keys():
        dfs(node)
        if node.color == "G":
            return False  # Cycle detected, cannot finish all courses

    return True

# BFS
# Case 1
# {'B': ['A'], 'C': ['A'], 'D': ['B', 'C']}
# Visiting node: B
# Visiting node: C
# Visiting node: D
# Visiting node: A
# True

def canFinish(graph) -> bool:
    n = len(graph)
    path = []
    q = collections.deque(graph)

    # Need to look whether there is a cycle in the graph or not 
    # All course should not have any cyclic dependencies -> use deg_cnt
    while q:
        v = q.popleft() # Give one vertex 
        path.append(v)
        if v.color == "G":
            return False # Cycle detected, cannot finish all courses 
        if v.color == "W":
            print("Visiting node:", v.id)
            v.color = "G"
            for w in graph.get(v, []): # for w in v.neighbors
                if w.color == "W":
                    q.append(w)
            v.color = "B"
    return True



if __name__ == "__main__":
    print("GNODE_207_CourseSchedule.py")
    print("\nCase 1")
    # Example usage:
    numCourses = 4
    prerequisites = [['B', 'A'], ['C', 'A'], ['D', 'B'], ['D', 'C']]
    A, B, C, D, E = GNode('A'), GNode('B'), GNode('C'), GNode('D'), GNode('E')
    # G = dict()
    # G[A], G[B], G[C] = [C, D] , [A, E], [B, D]
    G_2 = dict()
    G_2[B], G_2[C], G_2[D] = [A], [A], [B,C]

    print(_show_GNode(G_2))
    # result_1 = canFinish(G)
    # print(result_1) 
    result_2 = canFinish(G_2)
    print(result_2)  # Output: ['A', 'B', 'D', 'C'] / True




'''
Question

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

'''

# Original Answer BFS version
# def canFinish(numCourses, prerequisites):
#     # Create a graph with GNode instances
#     graph = {i: GNode(i) for i in range(numCourses)}

#     # Populate neighbors based on prerequisites
#     for course, pre in prerequisites:
#         graph[pre].neighbors.append(graph[course])

#     # Perform BFS to detect cyclic dependencies
#     for node in graph.values():
#         if node.color == "W":
#             queue = deque([node])
#             while queue:
#                 current = queue.popleft()
#                 if current.color == "G":
#                     return False  # Cycle detected, cannot finish all courses
#                 current.color = "G"
#                 for neighbor in current.neighbors:
#                     if neighbor.color == "W":
#                         queue.append(neighbor)
#                 current.color = "B"

#     return True