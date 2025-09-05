A, B = map(int, input().split())
C = int(input())

if B + C < 60:                     
    H = A
    M = B + C
else:
    H = (A + (B + C)//60) % 24
    M = (B + C) % 60

print(H, M)