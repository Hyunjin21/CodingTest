import sys
input = sys.stdin.readline

v, e = map(int, input().split())

parent = list(range(v + 1))
size = [1] * (v + 1) 
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

def find_parent(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union_parent(a, b):
    ra, rb = find_parent(a), find_parent(b)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True

result = 0
picked = 0
for cost, a, b in edges:
    if union_parent(a, b):
        result += cost
        picked += 1
        if picked == v - 1: 
            break

print(result)
