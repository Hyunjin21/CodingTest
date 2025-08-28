N = int(input())
height = list(map(int, input().split()))
stack = []
result = [0] * N

for i in range(N):
    while stack:
        if stack[-1][1] > height[i]:
            result[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append((i, height[i]))

print(*result)
