#Take a list of numbers as input and print only the first half of the list.
num = list(map(int,input("enter the list:").split()))
first_half = len(num)//2
print(num[:first_half])
