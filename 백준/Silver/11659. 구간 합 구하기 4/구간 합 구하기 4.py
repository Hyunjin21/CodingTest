import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

P = [0] * (N+1)
for i in range(1, N+1):
    P[i] = P[i-1] + arr[i-1]

for _ in range(M):
    l, r = map(int, input().split())
    print(P[r]-P[l-1])
