A = int(input())
B = int(input())
C = int(input())

multi = A*B*C
a = []
for i in str(multi):
    a.append(i)
print(a.count('0'))
print(a.count('1'))
print(a.count('2'))
print(a.count('3'))
print(a.count('4'))
print(a.count('5'))
print(a.count('6'))
print(a.count('7'))
print(a.count('8'))
print(a.count('9'))