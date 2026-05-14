def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if letter != i:
            answer += i
    return answer
    
    # return my_string.replace(letter, '')
    
    # answer = []
    # for i in my_string:
    #     if letter != i:
    #         answer.append(i)
    # return ''.join(answer)