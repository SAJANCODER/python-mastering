arr = list(map(int,input("Enter the array:").split(" ")))
non_zero = [x for x in arr if x!=0]
zero = [0]*arr.count(0)
result = non_zero+zero
print(result)

