import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[b] = a
        return True
    return False

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    
    edges = []
    total = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))
        total += z
    edges.sort()
    
    parent = list(range(m))
    cost = 0
    for z, x, y in edges:
        if union(x, y):
            cost += z

    print(total-cost)