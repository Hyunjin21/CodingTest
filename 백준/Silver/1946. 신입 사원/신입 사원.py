import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    people = []
    for _ in range(N):
        paper, interview = map(int, input().split())
        people.append([paper, interview])
    people.sort()
    cnt = 1
    best = people[0][1]
    for i in range(1, N):
        if people[i][1] < best:
            cnt += 1
            best = people[i][1]
    print(cnt)
