N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
sortedB = sorted(range(N), key=lambda i: B[i], reverse = True)

new_A = [0] * N
for i in range(N):
    new_A[sortedB[i]] = A[i]

S = 0
for j in range(N):
    S += new_A[j]*B[j]
print(S)
