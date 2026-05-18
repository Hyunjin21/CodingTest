def solution(numbers, direction):
    answer = []
    length = len(numbers)
    if direction == 'right':
        answer.append(numbers[length-1])
        for i in range(0, len(numbers)-1):
            answer.append(numbers[i])
    elif direction == 'left':
        for j in range(1, len(numbers)):
            answer.append(numbers[j])
        answer.append(numbers[0])
    return answer