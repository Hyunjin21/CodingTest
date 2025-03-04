a = []
for i in range(5):
    a.append(int(input()))
a.sort()
avg = sum(a)//len(a)
mid = a[(len(a)-1)//2]
print(avg)
print(mid)