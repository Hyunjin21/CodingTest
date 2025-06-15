N, M = map(int,input().split())
time = list(map(int,input().split()))
start = max(time)
end = sum(time)
ans = end

while start <= end:
    mid = (start+end)//2
    total = 0
    count = 1
    for i in time:
        if total+i > mid:
            count += 1
            total = i
        else:
            total += i
    if count <= M:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)
