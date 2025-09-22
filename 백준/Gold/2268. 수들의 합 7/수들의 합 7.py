import sys
input = sys.stdin.readline

def add(tree, idx, delta):
    size = len(tree) - 1
    while idx <= size:
        tree[idx] += delta
        idx += idx & -idx

def prefix_sum(tree, idx):
    total = 0
    while idx > 0:
        total += tree[idx]
        idx -= idx & -idx
    return total

def range_sum(tree, left, right):  
    if left > right: 
        left, right = right, left
    return prefix_sum(tree, right) - prefix_sum(tree, left - 1)

N, M = map(int, input().split())
A = [0] * (N + 1) 
tree = [0] * (N + 1)

for _ in range(M):
    t, i, x = map(int, input().split())
    if t == 0:
        j = x
        print(range_sum(tree, i, j))
    else:
        k = x
        delta = k - A[i]
        A[i] = k
        add(tree, i, delta)
