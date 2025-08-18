import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input().strip())
parent = list(range(N))
edges = []
total = 0
for i in range(N):
    row = input().strip()
    for j in range(N):
        ch = row[j]
        if 'a' <= ch <= 'z':
            weight = ord(ch) - ord('a') + 1
        elif 'A' <= ch <= 'Z':
            weight = ord(ch) - ord('A') + 27
        else:
            weight = 0

        total += weight
        if i != j and weight > 0:
            edges.append((weight, i, j))
edges.sort()

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

mst = 0
cnt = 0
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        mst += cost
        cnt += 1

if cnt == N - 1:
    print(total - mst)
else:
    print(-1)
