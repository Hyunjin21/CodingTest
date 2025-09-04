H, M = map(int, input().split())
if M-45 < 0:
    if H == 0:
        H = 23
    else:
        H -= 1
    M = (M - 45) + 60
else:
    M = M - 45

print(H, M)