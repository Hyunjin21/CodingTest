N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
graph = []

def dfs(start):
    if len(graph) == M:
        print(*graph)
        return
    for i in range(start, N):
        graph.append(nums[i])
        dfs(i+1)
        graph.pop()

dfs(0)