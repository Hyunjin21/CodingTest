def solution(balls, share):
    n = 1
    m = 1
    n_m = 1
    for i in range(1, balls+1):
        n *= i
    for j in range(1, share+1):
        m *= j
    for k in range(1, balls-share+1):
        n_m *= k
    answer = n / (n_m*m)
    return answer