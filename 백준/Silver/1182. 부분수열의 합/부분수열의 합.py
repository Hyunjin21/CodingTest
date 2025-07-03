N, S = map(int,input().split())
nums = list(map(int,input().split()))
cnt = 0

def dfs(idx, total):
    global cnt
    if idx == N:
        if total == S and graph:
            cnt += 1
        return

    graph.append(nums[idx])
    dfs(idx + 1, total + nums[idx])
    graph.pop()
    dfs(idx + 1, total)

graph = []
dfs(0, 0)
print(cnt)
