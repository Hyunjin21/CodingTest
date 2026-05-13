# import math

# def solution(numer1, denom1, numer2, denom2):
#     num = denom1*numer2 + denom2*numer1
#     denom = denom1*denom2
#     gcd = math.gcd(num, denom)
#     return [num//gcd, denom//gcd]

def solution(numer1, denom1, numer2, denom2):
    num = denom1*numer2 + denom2*numer1
    denom = denom1*denom2
    
    for i in range(min(num, denom), 1, -1):
        if num % i == 0 and denom % i == 0:
            num //= i
            denom //= i
            break
        
    answer = [num, denom]
    return answer