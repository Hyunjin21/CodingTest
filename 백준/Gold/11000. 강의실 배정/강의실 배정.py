import sys
import heapq
input = sys.stdin.readline

N = int(input())
table = [tuple(map(int,input().split())) for _ in range(N)]
table.sort()

room = []
heapq.heappush(room, table[0][1])

for i in range(1, N):
    start, end = table[i]
    
    if room[0] <= start:
        heapq.heappop(room)
    heapq.heappush(room, end)

print(len(room))
