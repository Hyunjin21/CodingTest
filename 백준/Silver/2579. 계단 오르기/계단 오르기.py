N = int(input())
s = []
for _ in range(N):
    num = int(input())
    s.append(num)

dp = [0] * (N+1)
if N >= 1:
    dp[0] = s[0]
if N >= 2:
    dp[1] = s[0] + s[1]
if N >= 3:
    dp[2] = max(s[0]+s[2], s[1]+s[2])
for i in range(3, N):
    dp[i] = max(dp[i-2] + s[i], dp[i-3] + s[i-1] + s[i])

print(dp[N-1])