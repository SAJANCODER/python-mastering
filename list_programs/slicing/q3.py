#Print the list after removing the first and last elements using slicing.
num = list(map(int,input("enter the list:").split()))
remove = num[1:-1]
print(remove)