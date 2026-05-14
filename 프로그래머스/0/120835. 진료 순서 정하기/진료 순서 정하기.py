def solution(emergency):
    answer = []
    for i in emergency:
        index = 1
        for j in emergency:
            if i < j:
                index += 1
        answer.append(index)
    return answer