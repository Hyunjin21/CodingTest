T = int(input())
for i in range(1, T+1):
    s = input()
    year = s[:4]
    month = s[4:6]
    day = s[6:]
    print('#', end="")
    print(i, end=" ")
    if int(month) < 1 or int(month) > 12:
        print(-1)
    elif int(month) == 2 and int(day) > 28:
        print(-1)
    else:
        print(year + '/' + month + '/' + day)
       
        
