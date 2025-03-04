a = []
for i in range(9):
    a.append(int(input()))
a.sort()
b = sum(a)
for i in range(9):
    for j in range(9):
        if i!=j:
            if (b-a[i]-a[j])==100:
                for k in range(9):
                    if k!=i and k!=j:
                        print(a[k])
                exit()
      