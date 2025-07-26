import sys
input = sys.stdin.readline

N, S = map(int,input().split())
num = list(map(int,input().split()))
total = 0
end = 0
min_len = float('inf')

for start in range(N):
    while total < S and end < N:
        total += num[end]
        end += 1
    if total >= S:
        min_len = min(min_len, end-start)
    total -= num[start]

if min_len == float('inf'):
    print(0)
else:
    print(min_len)
