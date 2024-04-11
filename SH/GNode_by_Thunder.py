## Author : Jeongsik Pyo
## Date   : 2023-12-26
## Lang   : Python

class GNode:
    def __init__(self, id, color = "W", p = None):
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
        return self.id
  
    def __hash__(self):
        return hash(self.id)
    
    def reset(self):
        self.id = id
        self.color = "W"
        self.parent = None
    

######################## utils ########################
def _show_GNode(G: dict) -> dict:
    #0. set params 
    res = {}
    for key in G.keys():
        key_id = key.id
        items_id_list = []
        for item in G[key]:
            items_id_list.append(item.id)
        # print(key_id)
        # print(items_id_list)
        res[key_id] = items_id_list
        # print(res)
    return res

###### BFS ######
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

###### DFS ######
def _dfs(G: dict, s: GNode):
    stack = [s]
    path = []
    
    while stack:
        node = stack.pop()
        if node.color == "W":
            path.append(node.id)
            node.color = "B"
            stack.extend(neighbor for neighbor in G.get(node, []) if neighbor.color == "W")
    
    return path

def _dfs_reset(G: dict):
    for node in G.keys():
        node.color = "W"
        node.parent = None
    return None

############################################################

## find_rood_veritics function 
def find_root_vertices (G):
    root_list = []
    key_list = []
    for key in G.keys():
        key_list.append(key.id)
    key_list = sorted(key_list)
    # print("key_list: ", key_list)

    for key in G.keys():
        # print("#####", key.id, "#####")
        target_path = _bfs(G, key)
        if target_path == key_list:
            root_list.append(key.id)
        _bfs_reset(G)

    return root_list



###########################################################
# DFS for directed graph
# Python3 program to print DFS traversal
# from a given graph
from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# Default dictionary to store graph
		self.graph = defaultdict(list)

	
	# Function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	
	# A function used by DFS
	def DFSUtil(self, v, visited):

		# Mark the current node as visited
		# and print it
		visited.add(v)
		print(v, end=' ')

		# Recur for all the vertices
		# adjacent to this vertex
		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)

	
	# The function to do DFS traversal. It uses
	# recursive DFSUtil()
	def DFS(self, v):

		# Create a set to store visited vertices
		visited = set()

		# Call the recursive helper function
		# to print DFS traversal
		self.DFSUtil(v, visited)


# Driver's code
if __name__ == "__main__":
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Following is Depth First Traversal (starting from vertex 2)")
	
	# Function call
	g.DFS(2)

# This code is contributed by Neelam Yadav
