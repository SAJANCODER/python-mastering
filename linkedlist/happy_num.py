n = input("Enter a number:")
sum = 0
sum_lst = []
for i in n:
    sum +=int(i)**2
while sum>1:
    mav = 0
    for j in str(sum):
        mav+=int(j)**2
    sum = mav
    if sum==1:
        print("True")
        break
    if sum in sum_lst:
        print("False")
        break
    sum_lst.append(sum)
