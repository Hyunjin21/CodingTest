a, b, c = map(int,input().split())
if a==b==c:
    money = 10000 + a*1000
    print(money)
elif a==b and a!=c:
    money = 1000 + a*100
    print(money)
elif b==c and a!=b:
    money = 1000 + b*100
    print(money)
elif c==a and c!=b:
    money = 1000 + c*100
    print(money)
else:
    if a>b and a>c:
        print(a*100)
    if b>a and b>c:
        print(b*100)
    if c>a and c>b:
        print(c*100)
