import bisect
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
M_list = list(map(int, input().split()))

for target in M_list:
    idx = bisect.bisect_left(A, target)
    if idx < N and A[idx] == target:
        print(1)
    else:
        print(0)