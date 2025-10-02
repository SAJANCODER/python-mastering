num = list(map(int,input("enter the number:").split()))
smallest = num[0]
second_smallest = num [1]
for i in num:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif i < second_smallest and i!= smallest:
        second_smallest = i
print(smallest)
print(f"Second Smallest : {second_smallest}")