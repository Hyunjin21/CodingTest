from collections import deque
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    for y in range(N):
        for x in range(M):
            if tomato[y][x] == 1:
                queue.append((x, y))
    day = 0
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N and tomato[ny][nx] == 0:
                tomato[ny][nx] = tomato[cy][cx] + 1
                day = max(day, tomato[ny][nx])
                queue.append((nx, ny))
    return day

result = bfs()
for row in tomato:
    if 0 in row:
        print(-1)
        break
else:
    if result == 0:
        print(0)
    else:
        print(result - 1)   