import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
empty = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
row = [set() for _ in range(9)]
col = [set() for _ in range(9)]
box = [set() for _ in range(9)]

for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num != 0:
            row[i].add(num)
            col[j].add(num)
            box[(i // 3) * 3 + (j // 3)].add(num)

found = False
def dfs(depth):
    global found
    if found: return
    if depth == len(empty):
        for line in board:
            print(*line)
        found = True
        return

    y, x = empty[depth]
    b = (y // 3) * 3 + (x // 3)  

    for num in range(1, 10):
        if num not in row[y] and num not in col[x] and num not in box[b]:
            board[y][x] = num
            row[y].add(num)
            col[x].add(num)
            box[b].add(num)
            dfs(depth + 1)
            board[y][x] = 0
            row[y].remove(num)
            col[x].remove(num)
            box[b].remove(num)

dfs(0)
