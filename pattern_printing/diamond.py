# to print 

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

n = int(input("Enter a number:"))
for i in range(1,n+1):
    print((n-i)*" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
new = n-1
for x in range(new,0,-1):
    print((n-x)*" ",end="")
    for k in range(2*x-1):
        print("*",end="")
    print()