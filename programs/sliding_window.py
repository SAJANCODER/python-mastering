n = int(input("Enter the length: "))
arr = list(map(int,input("Enter the array elements: ").split(" ")))
k = int(input("Enter the window  size :"))
i = 0
total_window = n-k+1
new_max = []
for i in range(total_window):
    window_num = arr[i:k+i]
    max1 = window_num[0]
    for j in window_num:
        if j>max1:
            max1=j
    new_max.append(max1)

print(new_max)
        
