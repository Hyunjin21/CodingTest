import sys
input = sys.stdin.readline

INF = 10**19

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
minTree = [INF] * (N * 4)
maxTree = [-INF] * (N * 4)

def init_min(start, end, idx):
    if start == end:
        minTree[idx] = arr[start]
        return minTree[idx]
    mid = (start + end) // 2
    minTree[idx] = min(init_min(start, mid, idx * 2), init_min(mid + 1, end, idx * 2 + 1))
    return minTree[idx]

def init_max(start, end, idx):
    if start == end:
        maxTree[idx] = arr[start]
        return maxTree[idx]
    mid = (start + end) // 2
    maxTree[idx] = max(init_max(start, mid, idx * 2), init_max(mid + 1, end, idx * 2 + 1))
    return maxTree[idx]

def find_min(start, end, idx, left, right):
    if left > end or right < start:
        return INF
    if left <= start and end <= right:
        return minTree[idx]
    mid = (start + end) // 2
    return min(find_min(start, mid, idx * 2, left, right), find_min(mid + 1, end, idx * 2 + 1, left, right))

def find_max(start, end, idx, left, right):
    if left > end or right < start:
        return -INF
    if left <= start and end <= right:
        return maxTree[idx]
    mid = (start + end) // 2
    return max(find_max(start, mid, idx * 2, left, right), find_max(mid + 1, end, idx * 2 + 1, left, right))

init_min(0, N - 1, 1)
init_max(0, N - 1, 1)

for _ in range(M):
    a, b = map(int, input().split())
    l, r = a - 1, b - 1 
    ans_min = find_min(0, N - 1, 1, l, r)
    ans_max = find_max(0, N - 1, 1, l, r)
    print(ans_min, ans_max)