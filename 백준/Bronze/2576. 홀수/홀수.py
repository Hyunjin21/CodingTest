a = []
for i in range(7):
    a.append(int(input()))
b = []
for i in range(7):
    if a[i]%2 != 0:
        b.append(a[i])    
        
if len(b)==0:
    print(-1)
else:
    b.sort()
    print(sum(b))
    print(min(b))
   