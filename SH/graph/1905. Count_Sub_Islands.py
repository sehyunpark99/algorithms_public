'''
1905. Count Sub Islands
Medium
Topics
Companies
Hint
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.
'''
from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row, col = len(grid1), len(grid1[0]) # assume that both grid1 and grid2 have same dimension
        count = 0
        islands = []
        # visited1 = [[0 for _ in range(col)] for _ in range(row)]
        # visited2 = [[0 for _ in range(col)] for _ in range(row)]

        def dfs(x, y):
            # Stop case
            if (x<0 or x>=row) or (y<0 or y>=col) or grid2[x][y] == 0:
                return 
            grid2[x][y] = 0 # mark as visited
            # go through all the adjacent nodes
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x-1, y)
            dfs(x, y-1)

        # Removing all non-common sub-islands
        for i in range(row):
            for j in range(col):
                # if grid2 == 1 and grid1 == 0, it can never be sub-class of it
                if(grid1[i][j] == 0 and grid2[i][j] == 1):
                    dfs(i, j)
            
        # count common sub-islands
        for i in range(row):
            for j in range(col):
                if(grid1[i][j] == 1 and grid2[i][j] == 1):
                    dfs(i, j)
                    count += 1
  
        return count



if __name__ == "__main__":
    print("1905. Count_Sub_Islands.py")

    solution = Solution()
    print("\nCase 1")

    grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
    grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    # A, B, C, D, E, F = GNode('A'), GNode('B'), GNode('C'), GNode('D'), GNode('E'), GNode('F')
    # G = dict()
    # G[A], G[B], G[C], G[D], G[E] = [D], [D], [E], [C], [D]
    # print(_show_GNode(G))
    res = solution.countSubIslands(grid1, grid2)  # Output: 3
    ans = 3
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 2")
    grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
    grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    res = solution.countSubIslands(grid1, grid2)  # Output: -1
    ans = 2
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 2")
    grid1 = [[1,1,1,1,0,0],[1,1,0,1,0,0],[1,0,0,1,1,1],[1,1,1,0,0,1],[1,1,1,1,1,0],[1,0,1,0,1,0],[0,1,1,1,0,1],[1,0,0,0,1,1],[1,0,0,0,1,0],[1,1,1,1,1,0]]
    grid2 = [[1,1,1,1,0,1],[0,0,1,0,1,0],[1,1,1,1,1,1],[0,1,1,1,1,1],[1,1,1,0,1,0],[0,1,1,1,1,1],[1,1,0,1,1,1],[1,0,0,1,0,1],[1,1,1,1,1,1],[1,0,0,1,0,0]]
    res = solution.countSubIslands(grid1, grid2)  # Output: -1
    ans = 0
    print(res, "\n  ==> check: ", res==ans)

