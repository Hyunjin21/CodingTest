import sys
input = sys.stdin.readline

INF = 10**19
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
minTree = [INF] * (N * 4)

def init_min(start, end, idx):
    if start == end:
        minTree[idx] = arr[start]
        return minTree[idx]
    mid = (start + end) // 2
    minTree[idx] = min(init_min(start, mid, idx * 2), init_min(mid + 1, end, idx * 2 + 1))
    return minTree[idx]

def find_min(start, end, idx, left, right):
    if right < start or end < left:
        return INF
    if left <= start and end <= right:
        return minTree[idx]
    mid = (start + end) // 2
    return min(find_min(start, mid, idx * 2, left, right), find_min(mid + 1, end, idx * 2 + 1, left, right))

init_min(0, N - 1, 1)

for _ in range(M):
    a, b = map(int, input().split())
    l, r = a - 1, b - 1
    print(str(find_min(0, N - 1, 1, l, r)))
