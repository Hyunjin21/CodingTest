import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
node = [0] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, [distance[start], start])
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for next_node, next_dist in graph[now]:
            cost = dist + next_dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                node[next_node] = now
                heapq.heappush(q, [cost, next_node])

    return distance

dist_start = dijkstra(start)
path = []
curr = end
while curr:
    path.append(curr)
    curr = node[curr]
path.reverse()

print(dist_start[end])
print(len(path))
print(" ".join(map(str, path)))