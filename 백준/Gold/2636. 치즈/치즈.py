import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
cheeze = [list(map(int,input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
last_cnt = 0

while True:
    current = 0
    for i in cheeze:
        current += i.count(1)

    if current == 0:
        print(time)
        print(last_cnt)
        break

    last_cnt = current

    visited =[[False]*M for _ in range(N)]
    q = deque([(0,0)])
    visited[0][0] = True

    melt = []
    while q:
        x, y = q.popleft()
        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]
            if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            if cheeze[nx][ny] == 0:
                q.append((nx, ny))
            elif cheeze[nx][ny] == 1:
                melt.append((nx, ny))

    for x, y in melt:
        cheeze[x][y] = 0

    time += 1
