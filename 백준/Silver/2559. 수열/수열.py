import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp = list(map(int, input().split()))

window = sum(temp[:K])
max_sum = window

for i in range(K, N):
    window += temp[i] - temp[i - K]
    max_sum = max(max_sum, window)

print(max_sum)