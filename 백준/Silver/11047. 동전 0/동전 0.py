N, K = map(int,input().split())
A = []
for _ in range(N):
    coin = int(input())
    A.append(coin)
A.sort(reverse = True)

cnt = 0
for i in A:
    if K == 0:
        break
    cnt += K // i
    K %= i
print(cnt)