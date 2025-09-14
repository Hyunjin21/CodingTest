import sys
input = sys.stdin.readline
from collections import deque

field = [list(input().strip()) for _ in range(12)]

H, W = 12, 6
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
ans = 0

def bfs(r, c, visited):
    color = field[r][c]
    q = deque([(r, c)])
    visited[r][c] = True
    group = [(r, c)]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and field[nx][ny] == color:
                visited[nx][ny] = True
                q.append((nx, ny))
                group.append((nx, ny))
    return group

while True:
    visited = [[False]*W for _ in range(H)]
    pop = []  
    for r in range(H):
        for c in range(W):
            if field[r][c] != '.' and not visited[r][c]:
                group = bfs(r, c, visited)
                if len(group) >= 4:
                    pop.extend(group)

    if not pop:
        break
    
    for r, c in pop:
        field[r][c] = '.'
        
    for c in range(W):
        w = H - 1
        for r in range(H - 1, -1, -1):
            if field[r][c] != '.':
                field[w][c] = field[r][c]
                w -= 1
        for r in range(w, -1, -1):
            field[r][c] = '.'
    ans += 1

print(ans)
