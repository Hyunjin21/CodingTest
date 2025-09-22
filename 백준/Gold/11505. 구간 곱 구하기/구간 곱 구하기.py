import sys
input = sys.stdin.readline

def merge(x, y):
    return (x * y) % 1000000007

def init(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = merge(init(start, mid, idx * 2), init(mid + 1, end, idx * 2 + 1))
    return tree[idx]

def find(start, end, idx, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[idx]
    mid = (start + end) // 2
    return merge(find(start, mid, idx * 2, left, right), find(mid + 1, end, idx * 2 + 1, left, right))

def update(start, end, idx, target, new_value):
    if target < start or target > end:
        return tree[idx]
    if start == end:
        tree[idx] = new_value
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = merge(update(start, mid, idx * 2, target, new_value), update(mid + 1, end, idx * 2 + 1, target, new_value))
    return tree[idx]

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [1] * (N * 4)

init(0, N - 1, 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b - 1] = c
        update(0, N - 1, 1, b - 1, c)
    else:
        print(find(0, N - 1, 1, b - 1, c - 1))
