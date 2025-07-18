import sys
input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n):
    name, log = input().split()
    dic[name] = log
    if log == 'leave':
        del dic[name]

result = sorted(dic.items(), reverse=True)

for key, value in result:
    print(key)