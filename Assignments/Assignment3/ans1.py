# 1. Python Program to Find Common Characters in Two Strings

# Method1-
str1 = str(input("Enter string1: "))
str2 = str(input("Enter string2: "))
common = []
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            common.append(str1[i])
ans = set(common)
if len(ans) == 0:
    print("No common characters")
else:
    print(ans)

#Method2-
str1 = str(input("Enter string1: "))
str2 = str(input("Enter string2: "))
st1 = set(str1)
st2 = set(str2)
common = st1.intersection(st2)
common = list(common)

print("Common chars -",common)