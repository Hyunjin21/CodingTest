n, m = map(int,input().split())
paint = [list(map(int,input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_stack(x, y):
    stack = [(x, y)]
    paint[y][x] = 0
    area = 1
    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n and paint[ny][nx] == 1:
                paint[ny][nx] = 0
                stack.append((nx,ny))
                area += 1
    return area

cnt = 0
max_area = 0
for y in range(n):
    for x in range(m):
        if paint[y][x] == 1:
            cnt += 1
            max_area = max(max_area, dfs_stack(x, y))
print(cnt)
print(max_area)
