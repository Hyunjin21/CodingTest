import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [ 0, 1, 0,-1]

cnt = 0
cleaned = [[False]*M for _ in range(N)]

while True:
    if not cleaned[r][c]:
        cleaned[r][c] = True
        cnt += 1

    moved = False
    for _ in range(4):
        d = (d + 3) % 4 
        nr = r + dr[d]
        nc = c + dc[d]
        if room[nr][nc] == 0 and not cleaned[nr][nc]:
            r, c = nr, nc
            moved = True
            break

    if moved:
        continue 

    back_dir = (d + 2) % 4
    br = r + dr[back_dir]
    bc = c + dc[back_dir]
    if room[br][bc] == 1: 
        break
    else:
        r, c = br, bc  

print(cnt)
