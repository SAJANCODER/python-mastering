arr = list(map(int,input("Enter the array:").split(" ")))
found = 0
while arr:
    
    found+=max(arr)
    arr.remove(found)
print(found)

        
