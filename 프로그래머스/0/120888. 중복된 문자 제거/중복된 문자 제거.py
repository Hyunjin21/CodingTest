def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    # answer = ''.join(dict.fromkeys(my_string))
    return answer