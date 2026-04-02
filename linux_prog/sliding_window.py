arr = [1,2,3,5,7]
k = 3
first_sum = sum(arr[:k])
max_sum = first_sum
for i in range(k,len(arr)):
	second_sum = max_sum + arr[i] - arr[i-k]
	max_sum = max(first_sum,second_sum)
print(max_sum)
