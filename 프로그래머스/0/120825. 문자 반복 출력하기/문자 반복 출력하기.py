def solution(my_string, n):
    answer = []
    my_string = list(my_string)
    for i in my_string:
        answer.append(i*n)
    return ''.join(answer)