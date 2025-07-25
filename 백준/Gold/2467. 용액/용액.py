import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
start, end = 0, N-1
value = float('inf')
left, right = 0, 0

while start < end:
    total = num[start] + num[end]

    if abs(total) <= value:
        left = num[start]
        right = num[end]
        value = abs(total)
    if total <= 0:
        start += 1
    else:
        end -= 1

print(left, right)