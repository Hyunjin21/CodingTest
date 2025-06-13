T = int(input())
for _ in range(T):
    N = int(input())
    start = 0
    end = N
    result = 0
    while start <= end:
        mid = (start+end)//2
        if (mid*(mid+1))//2 <= N:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    print(result)
