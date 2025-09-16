import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * (N * 4)

def init(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx * 2) + init(mid + 1, end, idx * 2 + 1)
    return tree[idx]


def find(start, end, idx, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[idx]
    mid = (start + end) // 2
    return find(start, mid, idx * 2, left, right) + find(mid + 1, end, idx * 2 + 1, left, right)


def update(start, end, idx, target, diff):
    if target < start or target > end:
        return
    tree[idx] += diff
    if start != end:
        mid = (start + end) // 2
        update(start, mid, idx * 2, target, diff)
        update(mid + 1, end, idx * 2 + 1, target, diff)

init(0, N - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        tmp = c - arr[b - 1]
        arr[b - 1] = c
        update(0, N - 1, 1, b - 1, tmp)
    else:
        print(find(0, N - 1, 1, b - 1, c - 1))
