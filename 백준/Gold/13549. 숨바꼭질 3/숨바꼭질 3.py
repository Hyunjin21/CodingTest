import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 100001

def bfs():
    queue = deque()
    queue.append((0, N))
    while queue:
        time, cur = queue.popleft()
        if cur == K:
            print(time)
            break
        jump = cur * 2
        back = cur - 1
        front = cur + 1

        if 0 <= jump <= 100000 and visited[jump] == 0:
            queue.appendleft((time, jump))
            visited[jump] = 1
        if 0 <= back <= 100000 and visited[back] == 0:
            queue.append((time+1, back))
            visited[back] = 1
        if 0 <= front <= 100000 and visited[front] == 0:
            queue.append((time+1, front))
            visited[front] = 1
            
bfs()