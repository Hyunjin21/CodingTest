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

N, Q = map(int, input().split())
arr = [0] + list(map(int, input().split())) 
tree = [0] * (N + 1)

for i in range(1, N + 1):
    add(tree, i, arr[i])

out = []
for _ in range(Q):
    x, y, a, b = map(int, input().split())
    out.append(str(range_sum(tree, x, y)))
    delta = b - arr[a]
    arr[a] = b
    add(tree, a, delta)

print("\n".join(out))