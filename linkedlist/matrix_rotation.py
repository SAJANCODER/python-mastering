x = int(input("enter the lengeth of the matrix: "))
matrix_arr = []
for i in range(x):
    arr = list(map(int,input(f"Enter the matrix value of row {i}: ").split(" ")))
    if len(arr)==x:
        matrix_arr.append(arr)
    else:
        print(f"{x}x{x} exceed" if len(x)>x else f"{x}x{x} is lesser")

            #Approach 1
# col = 0
# row = 0
# page = []
# final_arr = []
# for i in range(x):
#     for j in range(x):
#         page.append(matrix_arr[row][col])
#         row+=1
#     reverse = page[::-1]
#     final_arr.append(reverse)
#     row = 0
#     col+=1
#     page=[]
# for i in final_arr:
#     x=list(map(str,i))
#     print(" ".join(x))

                #Approach 2
page = []
final_arr = []
for i in range(len(matrix_arr)):
    for j in range(len(matrix_arr)-1,-1,-1):
        page.append(matrix_arr[j][i])
    final_arr.append(page)
    page=[]
for i in final_arr:
    m = list(map(str,i))
    print(" ".join(m))
