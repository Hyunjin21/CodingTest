import heapq
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = int(1e9)

def dijkstra():
    distance[0][0] = graph[0][0]
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))

    while q:
        cost, x, y = heapq.heappop(q)
        if x == N-1 and y == N-1:
            print(f"Problem {cnt}: {cost}")
            return      
        if cost > distance[x][y]:
            continue        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                new_cost = cost + graph[nx][ny]
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))

cnt = 1
while True:
    N = int(input())
    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]
    dijkstra()
    cnt += 1