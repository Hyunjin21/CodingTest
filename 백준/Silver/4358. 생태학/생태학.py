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

for key, value in sorted(dic.items()):
    percentage = (value/total)*100
    print(f"{key} {percentage:.4f}")