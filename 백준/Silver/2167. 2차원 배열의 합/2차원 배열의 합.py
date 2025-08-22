import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

P = [[0]*(M+1) for _ in range(N+1)]

for a in range(1, N+1):
    for b in range(1, M+1):
        P[a][b] = P[a][b-1] + P[a-1][b] - P[a-1][b-1] + arr[a-1][b-1]

for _ in range(K):
    i, j, x, y = map(int, input().split())
    answer = P[x][y] - P[i-1][y] - P[x][j-1] + P[i-1][j-1]
    print(answer)