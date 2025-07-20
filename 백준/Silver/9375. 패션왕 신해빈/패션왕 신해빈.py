import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    dic = {}
    for _ in range(n):
        name, kind = input().split()
        if kind in dic.keys():
            dic[kind] += 1
        else:
            dic[kind] = 1

    cnt = 1
    for i in dic:
        cnt *= (dic[i] + 1)
            
    print(cnt-1)
        