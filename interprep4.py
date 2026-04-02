#FIND SECOND LARGEST IN AN ARRAY
arr = list(map(int,input("Enter an array:").split(" ")))
xy = list(set(arr))
xy.sort()
print(xy[-2])
