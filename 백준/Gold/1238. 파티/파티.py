import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(N+1)]
re_graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v , t = map(int, input().split())
    graph[u].append((v, t))
    re_graph[v].append((u, t))

def dijkstra(X, graph):
    distance = [INF] * (N+1)
    distance[X] = 0
    q = []
    heapq.heappush(q, (0, X))

    while q:
        time, now = heapq.heappop(q)
        if distance[now] < time:
            continue
        for next_node, next_time in graph[now]:
            if time + next_time < distance[next_node]:
                distance[next_node] = time + next_time
                heapq.heappush(q, (distance[next_node], next_node))
    return distance

to_home = dijkstra(X, graph)
from_home = dijkstra(X, re_graph)

max_time = 0
for i in range(1, N+1):
    total = from_home[i] + to_home[i]
    max_time = max(max_time, total)
print(max_time)