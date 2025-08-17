import sys
input = sys.stdin.readline

def w(c):
    if c == '0':
        return 0
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 27

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

N = int(input().strip())
edges = []
total = 0
for i in range(N):
    s = input().strip()
    for j in range(N):
        L = w(s[j])
        total += L
        if i != j and L > 0:
            edges.append((L, i, j))

edges.sort()

parent = list(range(N))
size = [1] * N

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
