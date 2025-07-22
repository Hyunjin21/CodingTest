import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visit = list(map(int, input().split()))
num = sum(visit[:X])
term = []
term.append(num)

for i in range(X, N):
    num += visit[i] - visit[i-X]
    term.append(num)

max_sum = max(term)
cnt = 0
for j in term:
    if j == max_sum:
        cnt += 1
if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(cnt)