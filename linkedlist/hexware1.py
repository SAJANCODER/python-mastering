#Write a Python program to check whether a string is a palindrome.

a = input("Enter the string :")
b = a[::-1]
if a==b:
    print("Palindrone")
else:
    print("Not a palindrone")

#two sum
a = [2,7,11,15]
target = 9
hash = {}
for i in range(len(a)):
    rem = target - a[i]
    if rem in hash:
        print(i,hash[rem])
        break
    else:
        hash[a[i]] = i