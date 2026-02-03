#n=1212343
#o/p = yes

n=list(map(int,input("enter a number:")))
is_valid = False
for i in range(len(n)-1):
    if abs((n[i] - n[i+1])) == 1:
        is_valid = True
    else:
        is_valid = False
if is_valid:
    print("yes")
else:
    print("no")
