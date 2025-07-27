def is_palindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

T = int(input())
for _ in range(T):
    s = input().strip()
    l, r = 0, len(s) - 1
    answer = 0
    while l < r:
        if s[l] != s[r]:
            if is_palindrome(s, l + 1, r) or is_palindrome(s, l, r - 1):
                answer = 1  
            else:
                answer = 2 
            break
        l += 1
        r -= 1

    print(answer)