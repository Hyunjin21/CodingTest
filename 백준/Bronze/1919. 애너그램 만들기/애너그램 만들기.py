str1 = sorted(list(str(input())))
str2 = sorted(list(str(input())))
i = 0
j = 0
remain = 0
while i<len(str1) and j<len(str2):
    if str1[i] == str2[j]:
        i+=1
        j+=1
    elif str1[i]<str2[j]:
        remain += 1
        i+=1
    else:
        remain += 1
        j+=1     
remain += (len(str1)-i)+(len(str2)-j)
print(remain)