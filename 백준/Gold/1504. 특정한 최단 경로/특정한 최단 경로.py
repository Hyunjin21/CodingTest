import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] *(N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

d1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

path1 = d1[v1] + dist_v1[v2] + dist_v2[N]
path2 = d1[v2] + dist_v2[v1] + dist_v1[N]

result = min(path1, path2)
print(result if result < INF else -1)