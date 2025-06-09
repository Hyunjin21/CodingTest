N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
M_list = list(map(int,input().split()))

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start+end)//2

        if data[mid] == target:
            return 1
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in M_list:
    if binary_search(i, A):
        print(1)
    else:
        print(0)
