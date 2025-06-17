N = int(input())
house = [list(map(int, input())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    stack = [(x, y)]
    house[y][x] = 0
    area = 1
    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and house[ny][nx] == 1:
                house[ny][nx] = 0
                stack.append((nx, ny))
                area += 1
    return area

cnt = 0
area_list = []
for y in range(N):
    for x in range(N):
        if house[y][x] == 1:
            cnt += 1
            area_list.append(dfs(x, y))

print(cnt)
area_list.sort()
for i in area_list:
    print(i)