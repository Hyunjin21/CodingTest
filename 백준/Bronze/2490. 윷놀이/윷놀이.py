for i in range(3):
    a, b, c, d = map(int,input().split())
    score = a+b+c+d
    if score == 3:
        print('A')
    elif score == 2:
        print('B')
    elif score == 1:
        print('C')
    elif score == 0:
        print('D')
    elif score == 4:
        print('E')
    