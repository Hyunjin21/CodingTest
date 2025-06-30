N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
visited = [False]*N
depth = []

def dfs():
    if len(depth) == M:
        print(*depth)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            depth.append(nums[i])
            dfs()
            depth.pop()
            visited[i] = False

dfs()