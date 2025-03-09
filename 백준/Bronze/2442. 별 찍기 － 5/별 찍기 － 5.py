N = int(input())
for i in range(N):
    if i==N:
        print(' '*(N-1-i) + '*'*(2*i+1))
    else:
        print(' '*(N-1-i) + '*'*(2*i+1) + ' ')