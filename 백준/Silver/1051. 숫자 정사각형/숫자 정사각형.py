import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

side = 1 
for k in range(2, min(N, M) + 1):
    for i in range(N - k + 1):
        for j in range(M - k + 1):
            c = grid[i][j]
            if (c == grid[i][j + k - 1] and c == grid[i + k - 1][j] and c == grid[i + k - 1][j + k - 1]):
                side = k
print(side * side)
