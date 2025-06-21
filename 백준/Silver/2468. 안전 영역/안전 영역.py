from collections import deque
N = int(input())
height = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, rain):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[ny][nx] and height[ny][nx] > rain:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

max_safe = 0
for rain in range(0, 101):
    visited = [[False] *N for _ in range(N)]
    cnt = 0   
    for y in range(N):
        for x in range(N):
            if not visited[y][x] and height[y][x] > rain:
                bfs(x, y, rain)
                cnt += 1
    max_safe = max(max_safe, cnt)

print(max_safe)