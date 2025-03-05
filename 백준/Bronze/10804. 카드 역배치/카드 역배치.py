li = []
for i in range(1,21):
    li.append(i)
for n in range(10):
    a, b = map(int,input().split())
    if a==1:
        li[a-1:b] = li[b-1::-1]
    elif a==1 and b==20:
        li[::-1]
    else:
        li[a-1:b] = li[b-1:a-2:-1]
    
print(*li)    