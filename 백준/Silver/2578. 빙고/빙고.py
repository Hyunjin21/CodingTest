import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
calls = []
for _ in range(5):
    calls += list(map(int, input().split()))

def bingo():
    cnt = 0
    for i in range(5):
        if all(board[i][j] == 0 for j in range(5)):
            cnt += 1
    for j in range(5):
        if all(board[i][j] == 0 for i in range(5)):
            cnt += 1
    if all(board[i][i] == 0 for i in range(5)):
        cnt += 1
    if all(board[i][4-i] == 0 for i in range(5)):
        cnt += 1
    return cnt

for i in range(25): 
    for x in range(5):
        for y in range(5):
            if calls[i] == board[x][y]:
                board[x][y] = 0
                break
        else:
            continue
        break

    if bingo() >= 3:
        print(i+1)
        break
