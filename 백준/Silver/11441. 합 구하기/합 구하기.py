import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

P = [0] * (N+1)
for k in range(1, N+1):
    P[k] = P[k-1] + arr[k-1]

for _ in range(M):
    i, j = map(int,input().split())
    print(P[j] - P[i-1])