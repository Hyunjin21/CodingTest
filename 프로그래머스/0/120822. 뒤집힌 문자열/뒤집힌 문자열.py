def solution(my_string):
    answer = list(my_string)
    answer.reverse()
    return ''.join(answer)

    # return ''.join(reversed(my_string))
    
    # return my_string[::-1]