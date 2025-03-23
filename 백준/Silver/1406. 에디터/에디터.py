import sys
str1 = list(sys.stdin.readline().rstrip())
str2 = []
M = int(sys.stdin.readline())
for i in range(M):
    pwd = list(sys.stdin.readline().split())
    if pwd[0] == 'P':
        str1.append(pwd[1])
    elif pwd[0] == 'L':
        if str1:
            str2.append(str1.pop())
    elif pwd[0] == 'D':
        if str2:
            str1.append(str2.pop())
    else:
        if str1:
            str1.pop()
    
str1.extend(reversed(str2))
print(''.join(str1))