import bisect
N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
targets = list(map(int, input().split()))

def count_by_bisect(x):
    return bisect.bisect_right(cards, x) - bisect.bisect_left(cards, x)

for i in targets:
    print(count_by_bisect(i), end=' ')