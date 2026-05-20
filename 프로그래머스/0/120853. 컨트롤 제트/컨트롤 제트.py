def solution(s):
    answer = 0
    string = s.split(' ')
    for i in range(len(string)):
        if string[i] == 'Z':
            answer -= int(string[i-1])
        else:
            answer += int(string[i])
    return answer