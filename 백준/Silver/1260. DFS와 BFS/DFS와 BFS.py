from collections import deque
N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for edges in graph:
    edges.sort()

visited1 = [False] * (N+1)
def dfs(V):
    visited1[V] = True
    print(V, end=' ')
    for i in graph[V]:
        if not visited1[i]:
            dfs(i)

visited2 = [False] * (N+1)
def bfs(start):
    queue = deque([start])
    visited2[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited2[i]:
                visited2[i] =True
                queue.append(i)

dfs(V)
print()
bfs(V)