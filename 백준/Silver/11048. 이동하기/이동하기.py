N, M = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        right = dp[i][j-1] if j > 0 else 0
        down = dp[i-1][j] if i > 0 else 0
        diagon = dp[i-1][j-1] if i > 0 and j > 0 else 0
        dp[i][j] = max(right, down, diagon) + maze[i][j]

print(dp[N-1][M-1])