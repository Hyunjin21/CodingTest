while True:
    line = input()
    if line == '0':
        break
    arr = list(map(int,line.split()))
    K, nums = arr[0], arr[1:]
    graph = []

    def dfs(start):
        if len(graph) == 6:
            print(*graph)
            return
        for i in range(start, K):
            graph.append(nums[i])
            dfs(i+1)
            graph.pop()

    dfs(0)
    print()
