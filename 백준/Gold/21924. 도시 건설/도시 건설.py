import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
total = 0
for i in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    total += c
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

cost = 0
cnt = 0
for c, a, b in edges:
    if union(a, b):
       cost += c
       cnt += 1
       if cnt == N-1:
           break
        
if cnt == N-1:
    print(total-cost)
else:
    print(-1)
