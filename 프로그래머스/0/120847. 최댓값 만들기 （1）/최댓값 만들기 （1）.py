def solution(numbers):
    arr = sorted(numbers, reverse=True)
    answer = arr[0]*arr[1]
    return answer