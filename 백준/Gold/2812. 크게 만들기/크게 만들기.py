N, K = map(int,input().split())

nums = list(input())
result = []

for i in nums:
    while len(result) > 0 and result[-1] < i and K > 0:
        result.pop()
        K -= 1
    result.append(i)

while K > 0:
    result.pop()
    K -= 1

print(''.join(result))