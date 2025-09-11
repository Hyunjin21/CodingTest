import sys
input = sys.stdin.readline

M, n = map(int,input().split())
x, y = 0, 0
dir = 0
flag = True

for _ in range(n):
    command, value = input().split()
    if command == "TURN":
        if value == "0":
            dir = (dir + 1) % 4
        else:
            dir = (dir + 3) % 4
    else:
        d = int(value)
        if dir == 0:
            x += d
        elif dir == 1:
            y += d
        elif dir == 2:
            x -= d
        else:
            y -= d
        if not (0 <= x <= M and 0 <= y <= M):
            flag = False
            break

if flag:
    print(x, y)
else:
    print(-1)