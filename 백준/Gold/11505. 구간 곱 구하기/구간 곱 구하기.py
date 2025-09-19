import sys
input = sys.stdin.readline

def merge(x,y):
    return x * y

def init(node,left,right):
    if left == right:
        tree[node] = arr[left]
        return tree[node]
    mid = (left+right)//2
    tree[node] = merge(init(node*2,left,mid),init(node*2+1,mid+1,right)) % 1000000007
    return tree[node]

def find(node,left,right,x,y):
    if x <= left and right <= y:
        return tree[node]
    if y < left or x > right:
        return 1
    mid = (left + right) // 2
    return merge(find(node * 2, left, mid, x, y), find(node * 2 + 1, mid + 1, right, x, y)) % 1000000007

def update(node,left,right,x,y):
    if left == right == x:
        tree[node] = y
        return tree[node]
    if x < left or x > right:
        return tree[node]
    mid = (left+right)//2
    tree[node] = merge(update(node*2,left,mid,x,y), update(node*2+1,mid+1,right,x,y)) % 1000000007
    return tree[node]

N, M, K = map(int,input().split())
arr = [int(input()) for _ in range(N)]
tree = [1] * (N*4+1)

init(1,0,N-1)

for _ in range(M+K):
    a, b, c = map(int,input().split())
    if a == 1:
        arr[b-1] = c
        update(1,0,N-1,b-1,c)
        continue
    print(find(1,0,N-1,b-1,c-1))