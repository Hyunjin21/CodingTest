N = int(input())
for i in range(N):
    print(' '*(N-1-i)+'*'*(2*i+1)+' '*1)
for i in range(N-1):    
    print(' '*(i+1)+'*'*(2*(N-1)-2*i-1)+' '*1)