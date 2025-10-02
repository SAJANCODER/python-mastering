#finding largest number in a list

num=list(map(int,input("enter the numbers:").split(" ")))
largest = num[0]
for i in num:
    if i>largest :
        largest = i
print(largest)

    
