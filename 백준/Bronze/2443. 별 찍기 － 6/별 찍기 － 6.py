N = int(input())
for i in range(N):
    if i==N:
        print(' '*i+'*'*(2*N-2*i-1)+' ')
    else:
        print(' '*i+'*'*(2*N-2*i-1)+' '*1)