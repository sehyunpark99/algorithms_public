from collections import deque 

class GNode:
    def __init__(self, id, color="W", d=0, p=None):
        # "W" = not visited, "G" = visited not all neighbors visited, 
        # "B" = all neighbors also visited
        self.id = id # id is a string
        self.color = color # color (status) of node
        self.distance = d
        self.parent = p

    def __str__(self):
        return self.id
    

def reset(G):
    for node in G:
        node.color = "W"
        node.parent = None

# BFS
# root is where all node can be visited
def find_root_vertices(G: dict) -> list:
    # path = []
    # q = deque(G) # objects, all elements are in the order where it has been assigned
    nodes = [i.id for i in G.keys()]
    ans = []

    for i in G.keys():
        q = deque([i])
        path = set()
        while q:
            curr = q.popleft()
            path.add(curr.id)
            # if the node has been visited -> cycle detected
            if curr.color == "G" or curr in path:
                continue
            if curr.color == "W":
                curr.color == "G"
                for w in G[curr]:
                    if w.color == "W":
                        q.append(w)
                curr.color = "B"
        reset(G)
        if len(path) == len(nodes):
            ans.append(i.id)
    # print(ans) # if I didn't use print in the main function
    return ans


# DFS
def find_root_vertices(G):
    cmp = []
    for node in G.keys():
        cmp.append(node.id)

    def dfs(node, path):
        path.add(node.id)
        if node.color == "W":
            node.color = "G"
            for w in G.get(node, []):
                if w.color == "W":
                    dfs(w, path)
            node.color = "B"
    ans = []
    for node in G.keys():
        path = set()
        if node.color == "W": #not visited
            dfs(node, path)

        if len(path) == len(cmp):
            ans.append(node.id)

        reset(G)

    return ans

if __name__ == "__main__":
    print("QE_23_09.py")
    print("\nCase 1")
    # Example usage:
    A, B, C = GNode('A'), GNode('B'), GNode('C')
    D, E, F = GNode('D'), GNode('E'), GNode('F')
    G = dict()
    G[A], G[B], G[C] = [C, D], [A,E], [B, D]
    G[D], G[E], G[F] = [F], [F], []
    result = find_root_vertices(G) # Output: ['A', 'B', 'C']
    print(result)

    print("\nCase 2")
    A, B, C = GNode('A'), GNode('B'), GNode('C')
    D, E, F = GNode('D'), GNode('E'), GNode('F')
    G = dict()
    G[A], G[B], G[C] = [D], [E], [B, D]
    G[F] = []
    G[D], G[E] = [F], [F]
    result = find_root_vertices(G) # Output: []
    print(result)

# The other
class GNode:
    def __init__(self, id, color="W", p=None):
        self.id = id #id is a string
        self.color = color #color (status) of node
        self.parent = p

    def __str__(self):
        return self.id
    
    def __hash__(self):
        return hash(self.id)
    
def find_root_vertices(G)->list:
    ## Implement
    #BFS쓰기
    #node 최대 100개 
    #끝까지 다 돈다면 root임
    q = []
    answer = []
    for key in G.keys():
    #    print("if Root: ", key)
        #돌면서 root인지 아닌지 체크
        path = [key]
        q.append(key)
        while(q):
            v = q.pop(0) #A/C,D/B
            for w in G[v]: #C,D/D,B
                #print("for w in G[v]: ", w) #C,D/D,B
                if w not in path:
                    path.append(w) #path[A,C,D/B]
                    q.append(w) #q[C,D/B]
        if len(path)==len(G):
            answer.append(key.__str__())
    return answer