class Solution:
  def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    # Edge case: n=1, return [0]
    if n == 1:
        return [0]
    
    # Build adjacency list for the graph
    adj_list = {i: set() for i in range(n)}
    for u, v in edges:
        adj_list[u].add(v)
        adj_list[v].add(u)
    
    # Find all leaf nodes (i.e., nodes with degree 1)
    leaves = [i for i in range(n) if len(adj_list[i]) == 1]
    
    # Repeat until we are left with 1 or 2 nodes
    while n > 2:
        
        # Remove the current leaf nodes along with their edges
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = adj_list[leaf].pop()
            adj_list[neighbor].remove(leaf)
            
            # If the neighbor becomes a new leaf node, add it to the list
            if len(adj_list[neighbor]) == 1:
                new_leaves.append(neighbor)
        
        # Update the list of leaf nodes
        leaves = new_leaves
    
    # The remaining nodes are the roots of the MHTs
    return leaves
  
from collections import defaultdict
from utils.GNode_by_Thunder import GNode


def findMinHeightTrees(n, edges):
    if n == 1:
        return [0]

    # 그래프 생성
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, parent, depth):
        node.color = "G"
        node.parent = parent
        max_depth = depth
        for neighbor_id in graph[node.id]:
            neighbor = G[neighbor_id]
            if neighbor.color == "W":
                neighbor_depth = dfs(neighbor, node, depth + 1)
                max_depth = max(max_depth, neighbor_depth)
        node.color = "B"
        return max_depth

    # 루트 후보 노드 찾기
    G = [GNode(i) for i in range(n)]
    root_candidates = []
    max_depth = -1
    for node in G:
        if node.color == "W":
            depth = dfs(node, None, 0)
            if depth > max_depth:
                root_candidates = [node]
                max_depth = depth
            elif depth == max_depth:
                root_candidates.append(node)
    # MHT 루트 노드 찾기
    MHT_roots = []
    for candidate in root_candidates:
        candidate.reset()
        dfs(candidate, None, 0)

    for node in G:
        if node.color == "B":
            MHT_roots.append(node.id)

    return MHT_roots
