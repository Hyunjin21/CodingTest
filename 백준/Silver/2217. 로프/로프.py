N = int(input())
k = []
for _ in range(N):
    rope = int(input())
    k.append(rope)
k.sort(reverse = True)

weight = []
for i in range(N):
    weight.append(k[i]*(i+1))

print(max(weight))