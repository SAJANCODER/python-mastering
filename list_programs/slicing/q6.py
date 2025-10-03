#Given a list, print every 2nd element using slicing.
#Example: [10,20,30,40,50] → [20,40]
num = list(map(int,input("enter the list:").split()))
print(num[1::2])
