import sys
input = sys.stdin.readline

N = int(input())
dic = {}
for _ in range(N):
    name = input().rstrip()
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1

num = max(dic.values())
best = []
for key, value in dic.items():
    if value == num:
        best.append(key)

best.sort()
print(best[0])