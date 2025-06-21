from collections import deque
N = int(input())
paint = [list(input()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
vistied = []

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    color = paint[y][x]
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[ny][nx] and paint[ny][nx] == color:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

def count(paint):
    global visited
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                bfs(x, y)
                cnt += 1
    return cnt

# 일반인
print(count(paint))

# 적록색약
for y in range(N):
    for x in range(N):
        if paint[y][x] == 'R':
            paint[y][x] = 'G'
print(count(paint))
