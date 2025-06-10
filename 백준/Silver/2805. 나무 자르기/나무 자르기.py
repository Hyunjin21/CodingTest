N, M = map(int,input().split())
H = list(map(int, input().split()))
H.sort()

def binary_search(H):
    start = 0
    end = max(H)
    result = 0
    while start <= end:
        mid = (start+end)//2
        num = 0
        for i in H:
            if i > mid:
                num += i - mid
        if num >= M:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

print(binary_search(H))