import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))
start = 0
end = 0
total = 0
min_len = float('inf')

while True:
    if total >= S:
        min_len = min(min_len, end - start)
        total -= num[start]
        start += 1
    elif end == N:
        break
    else:
        total += num[end]
        end += 1

if min_len == float('inf'):
    print(0)
else:
    print(min_len)