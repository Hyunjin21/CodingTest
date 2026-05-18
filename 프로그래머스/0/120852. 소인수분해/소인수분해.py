def solution(n):
    k = 2
    answer = []
    while n > 1:
        if n % k == 0:
            answer.append(k)
            while n % k == 0:
                n //= k
        k += 1
    return answer

    # answer = []
    # for i in range(2, int(n**0.5)+1):
    #     while n % i == 0:
    #         answer.append(i)
    #         n //= i
    # if n > 1:
    #     answer.append(n)
    # return sorted(list(set(answer)))