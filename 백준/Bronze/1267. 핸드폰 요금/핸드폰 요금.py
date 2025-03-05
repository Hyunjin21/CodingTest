N = int(input())
time = list(map(int,input().split()))
Y = 0
M = 0
for i in time:
    Y = Y +(i//30 + 1)*10
    M = M +(i//60 + 1)*15

if Y>M:
    print('M',M)
elif Y==M:
    print('Y M',Y)
else:
    print('Y',Y)