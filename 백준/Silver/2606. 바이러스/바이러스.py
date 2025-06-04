C = int(input())
N = int(input())
arr = [[] for _ in range(C+1)]
for _ in range(N):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for edges in arr:
    edges.sort()

visited = [False]*(C+1)
v = 1
def dfs(v):
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            dfs(i)

dfs(v)
cnt = 0
for i in visited:
    if visited[i] == True:
       cnt += 1
print(cnt-1)