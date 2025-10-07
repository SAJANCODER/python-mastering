#Fibonacci
num = int(input("Enter a number:"))
a,b=0,1
for i in range(num):
    c = a+b
    print("Fibonacci :",c)
    a,b = b,c
print(f"Fibonacci of {num} is {c}")