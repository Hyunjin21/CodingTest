import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

P = [0] * (N+1)
for i in range(1, N+1):
    P[i] = P[i-1] + arr[i-1]

result = []
for _ in range(M):
    l, r = map(int, input().split())
    result.append(str(P[r]-P[l-1]))

print('\n'.join(result))
