import sys
input = sys.stdin.readline

S = list(input().strip())
E = list(input().strip())
e = len(E)
stack = []

for i in S:
    stack.append(i)
    if stack[len(stack)-e:len(stack)] == E:
        for _ in range(e):
            stack.pop()

if stack:
    print(*stack, sep='')
else:
    print("FRULA")