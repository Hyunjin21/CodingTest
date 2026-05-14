def solution(emergency):
    arr = sorted(emergency, reverse = True)
    answer = []
    for i in emergency:
        idx = arr.index(i)+1
        answer.append(idx)
    return answer
    
    # answer = []
    # for i in emergency:
    #     index = 1
    #     for j in emergency:
    #         if i < j:
    #             index += 1
    #     answer.append(index)
    # return answer