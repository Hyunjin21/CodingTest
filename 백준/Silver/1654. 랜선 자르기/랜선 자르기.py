K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

def binary_search(lines, N):
    start = 1
    end = max(lines)
    result = 0
    while start <= end:
        mid = (start + end)//2
        cnt = 0
        for i in lines:
            cnt += i//mid
        if cnt >= N:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

print(binary_search(lines, N))
