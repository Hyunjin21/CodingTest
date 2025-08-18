import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    parent = list(range(m))    

    edges = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))
    edges.sort()

    cost = 0
    for z, x, y in edges:
        if find(x) != find(y):
            union(x, y)
        else:
            cost += z

    print(cost)
