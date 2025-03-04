a, b = map(int,input().split())
A, B = min(a,b),max(a,b)
if B-A-1>0:
    print(B-A-1)
    for i in range(A+1,B):
        print(i, end=' ')
else:
    print(0)