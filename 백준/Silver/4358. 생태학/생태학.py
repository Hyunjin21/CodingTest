import sys
input = sys.stdin.readline

dic = {}
total = 0

while True:
    tree = input().rstrip()
    if not tree:
        break
    total += 1
    if tree in dic:
        dic[tree] += 1
    else:
        dic[tree] = 1

result = sorted(dic.items())
for key, value in result:
    percentage = (value/total)*100
    print(f"{key} {percentage:.4f}")