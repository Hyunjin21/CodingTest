N = int(input())
table = []
for _ in range(N):
    time = list(map(int,input().split()))
    table.append(time)

table.sort(key=lambda x : (x[1], x[0]))

cnt = 0
end_time = 0
for start, end in table:
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)