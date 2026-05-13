def solution(array):
    max_cnt = 0
    list = [0]*(max(array)+1)
    for i in array:
        list[i] += 1
        
    for j in list:
        if j == max(list):
            max_cnt += 1
    
    if max_cnt > 1:
        return -1
    else:
        return list.index(max(list))