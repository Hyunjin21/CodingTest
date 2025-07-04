N = int(input())

def prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def dfs(num):
    if len(str(num)) == N:
        print(num)
        return
    for i in range(1, 10):
        next_num = num*10 + i
        if prime(next_num):
            dfs(next_num)

for start in [2, 3, 5, 7]:
    dfs(start)
