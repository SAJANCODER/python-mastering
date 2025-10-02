#finding second largest in a list
num1 = list(map(int,input("enter the number :").split()))
print(num1)
largest = num1[0]
second_largest = num1[1]
print(largest , second_largest)
for i in num1:
    print(i)
    if i >largest:
        second_largest = largest #while find the largest , it store the value of the sencond largest
        largest = i
    elif i>second_largest and i!=largest and i!=second_largest:
        second_largest = i
print("largest:",largest)
print("second_largest:",second_largest)
