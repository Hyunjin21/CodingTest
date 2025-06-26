N = int(input())
dp = [5001]*(N+1)
dp[0] = 0

for i in range(1, N+1):
    if i >= 3:
        dp[i] = min(dp[i], dp[i-3]+1)
    if i >= 5:
        dp[i] = min(dp[i], dp[i-5]+1)

if dp[N] == 5001:
    print(-1)
else:
    print(dp[N])
