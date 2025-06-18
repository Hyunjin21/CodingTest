from collections import deque
F, S, G, U, D = map(int, input().split())
visited = [False] * (F + 1)

def bfs(start):
    queue = deque()
    queue.append((start, 0)) #(현재 층, 버튼 누른 횟수)
    visited[start] = True
    while queue:
        current, presses = queue.popleft()
        if current == G:
            return presses
        for move in [U, -D]:
            next_floor = current + move
            if 1 <= next_floor <= F and not visited[next_floor]:
                visited[next_floor] = True
                queue.append((next_floor, presses + 1))
    return -1

result = bfs(S)
if result == -1:
    print("use the stairs")
else:
    print(result)