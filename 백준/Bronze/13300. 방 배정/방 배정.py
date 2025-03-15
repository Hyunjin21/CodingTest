N, K = map(int,input().split())
sList = [[0,0] for _ in range(6)]
count = 0
for i in range(N):
    S, Y = map(int,input().split())
    sList[Y-1][S]+=1
for i in range(6):
    for j in range(2):
        if sList[i][j]%K == 0:
            count += sList[i][j]//K
        else:
            count += sList[i][j]//K + 1
print(count)