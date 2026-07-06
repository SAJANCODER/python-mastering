#Given an integer array nums, return True if any value appears at least twice, otherwise return False.
lst = list(map(int,input("Enter a the list:").split(" ")))
times = 0
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] == lst[j]:
            times+=1
            
print("True : ",times)
