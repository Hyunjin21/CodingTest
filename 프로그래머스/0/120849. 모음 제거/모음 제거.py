def solution(my_string):
    arr = ['a', 'e', 'i', 'o', 'u']
    for i in arr:
        my_string = my_string.replace(i, '')
    return my_string

    # answer = ''
    # for i in str(my_string):
    #     if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
    #         answer += i
    # return answer