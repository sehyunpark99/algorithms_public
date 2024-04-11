from collections import defaultdict


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

def countcomponent(n, graph):
    # adj_mat for 
    # graph = [[0 for _ in range(n)] for _ in range(n)]
    # graph = defaultdict(list)
    # for edge in edges:
    #     graph[edge[0]].append(edge[1])
    #     graph[edge[1]].append(edge[0])
    # print(graph)

    def dfs(node):
        if node.color == "W":
            node.color = "G"
            for neighbor in graph.get(node, []):
                dfs(neighbor)
            node.color = "B"

    # Perform DFS to detect cyclic dependencies
    n = 0
    for node in graph.keys():
        if node.color == "W":
            n += 1
        dfs(node)
        
    return n


if __name__ == "__main__":
    print("Mock_Q1.py")
    A, B, C, D, E, F = GNode('A'), GNode('B'), GNode('C'), GNode('D'), GNode('E'), GNode('F')
    
    print("\nCase 1")
    n = 5
    edges = [[0,1], [1, 2], [3, 4]]
    G = dict()
    G[A], G[B], G[D] = [B], [C], [E]
    # res = countcomponent(n, edges) 
    res = countcomponent(n, G) 
    ans = 2
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 2")
    n = 5
    edges = [[0,1], [1, 2], [2, 3], [3, 4]]
    res = countcomponent(n, edges)  
    ans = 1
    print(res, "\n  ==> check: ", res==ans)

