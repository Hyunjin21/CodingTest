import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c)) 

def dfs(node, total):
    visited[node] = True
    for next_node, cost in tree[node]:
        if not visited[next_node]:
            dfs(next_node, total + cost)
    distance[node] = total

visited = [False] * (n + 1)
distance = [0] * (n + 1)
dfs(1, 0)
farthest = distance.index(max(distance))

visited = [False] * (n + 1)
distance = [0] * (n + 1)
dfs(farthest, 0)

print(max(distance))
