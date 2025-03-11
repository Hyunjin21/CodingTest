S = input()
import string
lower = []
for i in string.ascii_lowercase:
    lower.append(i)
for i in lower:
    print(S.count(i), end=' ')