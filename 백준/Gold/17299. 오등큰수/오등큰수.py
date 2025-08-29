import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
stack = [0]
result = [-1] * N
cnt = Counter(A)

for i in range(N):
    while stack and cnt[A[stack[-1]]] < cnt[A[i]]:
        result[stack.pop()] = A[i]
    stack.append(i)

print(*result)
