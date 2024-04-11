


N = int(input().split())
fishes = [list(map(int, input().split())) for _ in range(N)]

# Initial Setting
for i in range(N):
    for j in range(N):
        if fishes[i][j] == 9:
            row, col = i, j
time = 0
size = 2
eat = 0

def dfs(fishes, i, j):
    # Stop case
    if i<0 or i>=N or j<0 or j>=N or fishes[i][j]>size:
        return
    fishes[i][j] = "0"
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        newR, newC = i+dx, j+dy
        dfs(fishes, newR, newC)
        time += 1
