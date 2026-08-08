n = int(input("Enter matrix length: "))
matrix = []
for i in range(n):
    arr = list(map(int,input(f"Enter the values of row {i}: ").split(" ")))
    matrix.append(arr)

top = 0
bottom = n-1
left = 0
right = len(matrix[0])-1
page = []

while top<=bottom and left<=right:
    for i in range(left,right+1):
        page.append(matrix[top][i])
    top +=1

    for x in range(top,bottom+1):
        page.append(matrix[x][right])
    right-=1

    if top<=bottom:
        for y in range(right,left-1,-1):
            page.append(matrix[bottom][y])
        bottom -=1
    if left<=right:
        for m in range(bottom,top-1,-1):
            page.append(matrix[m][left])
        left+=1
print(page)