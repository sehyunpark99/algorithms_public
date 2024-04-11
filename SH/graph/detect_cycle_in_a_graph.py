# Python program to detect cycle
# in a graph
 
from collections import defaultdict
 
 
class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def isCyclicUtil(self, v, visited, recStack):
 
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
 
        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        # The node needs to be popped from
        # recursion stack before function ends
        recStack[v] = False
        return False
 
    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False
 
 
# Driver code
if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    if g.isCyclic() == 1:
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")
 
# Thanks to Divyanshu Mehta for contributing this code
        

from collections import deque
 
 
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
 
    def addEdge(self, v, w):
        self.adj[v].append(w)
 
    def isCyclic(self):
        inDegree = [0] * self.V
        q = deque()
        visited = 0
 
        # Calculate in-degree of each vertex
        for u in range(self.V):
            for v in self.adj[u]:
                inDegree[v] += 1
 
        # Enqueue vertices with 0 in-degree
        for u in range(self.V):
            if inDegree[u] == 0:
                q.append(u)
 
        # BFS traversal
        while q:
            u = q.popleft()
            visited += 1
 
            # Reduce in-degree of adjacent vertices
            for v in self.adj[u]:
                inDegree[v] -= 1
                # If in-degree becomes 0, enqueue the vertex
                if inDegree[v] == 0:
                    q.append(v)
 
        return visited != self.V  # If not all vertices are visited, there is a cycle
 
 
# Main driver code
g = Graph(6)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(4, 5)
g.addEdge(5, 3)
 
if g.isCyclic():
    print("Graph contains a cycle.")
else:
    print("Graph does not contain a cycle.")
# This code is contributed by Rishabh Mathur