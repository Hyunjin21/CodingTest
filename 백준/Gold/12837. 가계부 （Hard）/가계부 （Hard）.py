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
    return prefix_sum(tree, right) - prefix_sum(tree, left - 1)

N, Q = map(int, input().split())
tree = [0] * (N + 1)

for _ in range(Q):
    t, p, q = map(int, input().split())
    if t == 1:
        add(tree, p, q)
    else:
        print(str(range_sum(tree, p, q)))

