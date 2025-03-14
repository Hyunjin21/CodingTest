N = int(input())
li = list(map(int,input().split()))[:N]
v = int(input())
count = 0
for i in li:
    if i==v:
        count+=1
print(count)