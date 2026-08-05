n = int(input("Enter the length: "))
arr = list(map(int,input("Enter the array elements: ").split(" ")))
k = int(input("Enter the window  size :"))
# i = 0
# total_window = n-k+1
# new_max = []
# for i in range(total_window):
#     window_num = arr[i:k+i]
#     max1 = window_num[0]
#     for j in window_num:
#         if j>max1:
#             max1=j
#     new_max.append(max1)

# print(new_max)
max1 = float('-inf')

total_win_size = n-k+1
for i in range(total_win_size):
    sum2 = 0
    window = arr[i:k+i]
    for j in window:
        sum2+=j
    max1 = max(max1,sum2)
    
print(max1)
