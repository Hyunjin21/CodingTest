import sys
input = sys.stdin.readline

S = str(input().rstrip())
q = int(input())

cnt = [[0] * 26]
for i in range(len(S)):
    cnt.append(cnt[len(cnt)-1][:])
    cnt[i+1][ord(S[i])-97] += 1

for _ in range(q):
    al, l, r = input().split()
    answer = cnt[int(r)+1][ord(al)-97] - cnt[int(l)][ord(al)-97]
    print(answer)
    