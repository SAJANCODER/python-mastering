arr = list(map(int,input("Enter the array:").split()))
total_sum = 0
for i in range(len(arr)):
    current_min = arr[i]
    current_max = arr[i]
    for j in range(i,len(arr)):
        if arr[j]> current_max:
            current_max=arr[j]
        if arr[j]<current_min:
            current_min = arr[j]
        total_sum+=(current_max-current_min)
print(total_sum)
            
