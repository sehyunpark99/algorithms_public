'''
200. Number of Islands
Solved
Medium
Topics
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        visited = [[0 for _ in range(c)] for _ in range(r)]
        ans = 0

        def dfs(x, y):
            if 0<=x<r and 0<=y<c and grid[x][y] == "1" and visited[x][y] == 0: #haven't visited
                visited[x][y] = 1 # mark as visited
                # go through all the adjacent nodes
                dfs(x+1, y)
                dfs(x, y+1)
                dfs(x-1, y)
                dfs(x, y-1)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and visited[i][j] == 0:
                  dfs(i, j)
                  ans += 1
        return ans

class Solution:
    def dfs(self, grid, i, j):
        # Stop case
        if (i<0 or i>=len(grid)) or (j<0 or j>=len(grid[0])) or grid[i][j] != '1':
            return
        grid[i][j] = "0"
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        for dx, dy in directions:
            newR, newC = i+dx, j+dy
            self.dfs(grid, newR, newC)

    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        if not grid:
            return 0
        island = 0 
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    island += 1
        return island

if __name__ == "__main__":
    print("200. Number of Islands.py")

    solution = Solution()
    print("\nCase 1")

    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]
    
    res = solution.numIslands(grid)  
    ans = 1
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 2")
    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]
    
    res = solution.numIslands(grid)  
    ans = 3
    print(res, "\n  ==> check: ", res==ans)
