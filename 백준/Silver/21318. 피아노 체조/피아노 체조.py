import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
Q = int(input())

temp = [0] * N
for i in range(len(li)-1):
    if li[i+1] < li[i]:
        temp[i] = 1

P = [0] * (N+1)
for i in range(1, N+1):
    P[i] = P[i-1] + temp[i-1]

for _ in range(Q):
    x, y = map(int, input().split())
    print(P[y-1] - P[x-1])