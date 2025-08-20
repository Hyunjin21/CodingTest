import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

P = [0] * (N+1)
for i in range(1, N+1):
    P[i] = P[i-1] + A[i-1]

for _ in range(Q):
    L, R = map(int, input().split())
    print(P[R] - P[L-1])