#fibinocci
n = int(input("Enter a number: "))
start = 0
start2=1
for i in range(n):
    print(start)
    total = start + start2
    start = start2
    start2=total
