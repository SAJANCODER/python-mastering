# n = int(input("Enter the input length: "))

m = list(map(int,input("Enter the values:").split(" ")))

largest = m[0]
second_largest = 0

for i in m:
    if i>largest:
        second_largest = largest
        largest = i
    elif i>second_largest:
        second_largest=i
    elif i!=largest:
        second_largest = i
        
print(largest,second_largest)