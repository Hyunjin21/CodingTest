import sys
input = sys.stdin.readline

N = int(input().strip())   
M = int(input().strip())   
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()               
parent = list(range(N + 1))
size = [1] * (N + 1)

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

ans = 0
picked = 0
for c, a, b in edges:
    if union(a, b):      
        ans += c
        picked += 1
        if picked == N - 1:
            break

print(ans)
