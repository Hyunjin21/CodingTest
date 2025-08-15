import sys
input = sys.stdin.readline

N = int(input())
edges = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(i+1, N):
        edges.append((row[j], i, j))
edges.sort()

parent = list(range(N))
size = [1] * N

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

result = 0
cnt = 0
for cost, a, b in edges:
    if union(a, b):
        result += cost
        cnt += 1
        if cnt == N-1:
            break
        
print(result)