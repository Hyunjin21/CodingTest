N = int(input())
for i in range(N):    
    if i==N:
        print('*'*(2*N-1))
    else:
        print('*'*(i+1)+' '*(2*N-2*i-2)+'*'*(i+1))
for i in range(N-1):
    print('*'*(N-1-i)+' '*(2*i+2)+'*'*(N-1-i))
