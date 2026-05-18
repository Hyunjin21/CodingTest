def solution(numbers, k):
    idx = 0
    idx = (k-1)*2 % len(numbers)
    return numbers[idx]