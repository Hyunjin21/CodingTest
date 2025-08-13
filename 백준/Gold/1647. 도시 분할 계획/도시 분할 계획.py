import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))
edges.sort()

parent = list(range(N+1))
size = [1] * (N+1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False
    if size[a] < size[b]:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]
    return True

total = 0
max_edge = 0
cnt = 0

for c, a, b in edges:
    if union(a, b):
        total += c
        max_edge = max(max_edge, c)
        cnt += 1
        if cnt == N-1:
            break

result = total - max_edge
print(result)
