arr = list(map(int,input("Enter the array:").split(" ")))
target = int(input("Enter the target value:"))
def two_sum(arr,target):	
	for i in range(len(arr)+1):
		for j in range(i+1,len(arr)):
			if arr[i]+arr[j] == target:
				return [i,j]
print(two_sum(arr,target))



