def solution(age):
    answer = ''
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    age = [int(i) for i in str(age)]
    for j in age:
        answer += alpha[j]
    return answer