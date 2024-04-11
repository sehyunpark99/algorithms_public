'''
1559. Detect Cycles in 2D Grid
Medium
Topics
Companies
Hint
Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false.
'''

# DFS
class Solution:
    def containsCycle(self, A: List[List[str]]) -> bool:
        R, C = len(A), len(A[0])
        visited = set()
        
        def neighbors(r, c):
            return [(i, j) for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)] if 0 <= i < R and 0 <= j < C and A[i][j] == A[r][c]]
        
        def dfs(r, c, x, prev, seen):
            if (r, c) in seen:
                return True
            seen.add((r, c))
            visited.add((r, c))

            for i, j in neighbors(r, c):
                if not prev or prev != (i, j):
                    if dfs(i, j, x, (r, c), seen):
                        return True
            return False
            
        
        for r in range(R):
            for c in range(C):
                if (r, c) not in visited:
                    seen = set()
                    if dfs(r, c, A[r][c], None, seen):
                        return True
        return False

# BFS
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rowSize=len(grid)
        colSize=len(grid[0])
        visit=set()

        def bfs(row,col):
            cur=grid[row][col]

            q=collections.deque()
            q.append((row,col,-1))
            visit.add((row,col))

            while len(q)!=0:
                r,c,p=q.popleft()

                for i,j in [[-1,0],[1,0],[0,1],[0,-1]]:
                    newRow=r+i
                    newCol=c+j
                    if 0<=newRow<rowSize and 0<=newCol<colSize and grid[newRow][newCol]==cur and (newRow,newCol) not in visit:
                        q.append((newRow,newCol,(r,c)))
                        visit.add((newRow,newCol))
                    elif (newRow,newCol) in visit and grid[newRow][newCol]==cur and p!=(newRow,newCol):
                        return True

        for i in range(rowSize):
            for j in range(colSize):
                if (i,j) not in visit:
                    if bfs(i,j):
                        return True
        return False