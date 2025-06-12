N = int(input())
budgets = list(map(int,input().split()))
M = int(input())

def binary_search(budgets):
    if sum(budgets) <= M:
        return max(budgets)
    start = 0
    end = max(budgets)
    result = 0
    while start <= end:
        mid = (start+end)//2
        total = 0
        for i in budgets:
            if i <= mid:
                total += i
            else:
                total += mid
        if total <= M:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result

print(binary_search(budgets))