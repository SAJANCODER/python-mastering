# # Given an N × N matrix, rotate it 90° clockwise.

# # Input
# # 1 2 3
# # 4 5 6
# # 7 8 9
# # Output
# # 7 4 1
# # 8 5 2
# # 9 6 3

# n = int(input("Enter the matrx length:"))
# arr = []
# for i in range(n):
#         x = list(map(int,input("Enter the matrix element: ").split(" ")))
#         if len(x)==n:
#               arr.append(x)
#         else:
#             print(f"{n}x{n} is exceed")
#             break
# for i in range(len(arr)):
#     if i==n-1:
#           x = arr[i-(n-1)]
#           arr[i-(n-1)] = arr[i]
#           arr[i] = x
# col = 0
# final_arr = []
# # n_arr = []
# # for i in range(len(arr)):
# #       arr_lst = list(map(str,arr[i]))
# #       n_arr.append(arr_lst)
# col =0
# row =0
# page = []
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         page.append(arr[col][row])
#         col+=1
#     row+=1
#     col=0

#     final_arr.append(page)
#     page=[]

# for i in final_arr:
#       m = list(map(str,i))
#       print(" ".join(m))

n = int(input("Enter the length: "))
arr = []
for i in range(n):
    lst = list(map(int,input("Enter the list elements: ").split(" ")))
    arr.append(lst)
col = 0
row = 0
page = []
final_arr = []
for i in range(len(arr)):
    for j in range(len(arr)):
        page.append(arr[col][row])
        col+=1
    row+=1
    col=0
    x = page[::-1]
    final_arr.append(x)
    page = []
for i in final_arr:
    print(i)