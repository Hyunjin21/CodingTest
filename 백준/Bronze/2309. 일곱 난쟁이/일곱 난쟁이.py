arr = []
for i in range(9):
    arr.append(int(input()))
arr.sort()
total = sum(arr)
for i in range(9):
    for j in range(i+1,9):
        if (total-arr[i]-arr[j])==100:
            a = arr[i]
            b = arr[j]
            break
arr.remove(a)
arr.remove(b)
for k in arr:
    print(k)