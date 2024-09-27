# 2. Python Program to Count Number of Vowels in a String using Sets

str1 = str(input("Enter a string: "))
vowels = set('aeiouAEIOU')
ans = 0
for i in str1:
    if i in vowels:
        ans+=1
print(ans)

