n = int(input("Eneter a number:"))
i,j=0,1
for _ in range(n):
    i,j = j,i+j
    print(i,end=" ")