n = int(input())
li = sorted(list(map(int, input().split())))
x = int(input())
count = 0

left = 0
right = n-1

while left < right:
    result = li[left] + li[right]
    if result == x:
        count += 1
        left += 1
    elif result > x:
        right -= 1
    else:
        left += 1
print(count)