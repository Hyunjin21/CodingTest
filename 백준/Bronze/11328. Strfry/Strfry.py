N = int(input())
for i in range(N):
    a, b = map(str,input().split())
    if sorted(a) == sorted(b):
        print('Possible')
    else:
        print('Impossible')