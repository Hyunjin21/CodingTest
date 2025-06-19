from collections import deque
T = int(input())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        cx, cy = queue.popleft()
        if cx == ex and cy == ey:
            return chess[cy][cx]
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < l and 0 <= ny < l and chess[ny][nx] == 0:
                chess[ny][nx] = chess[cy][cx] + 1
                queue.append((nx, ny))

for _ in range(T):
    l = int(input())
    chess = [[0]*l for _ in range(l)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    print(bfs(sx, sy))
