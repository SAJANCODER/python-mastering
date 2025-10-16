#Fibonacci
num = int(input("Enter a number:"))
a,b=0,1
for i in range(num):
    c = a + b
    print("Fibonacci :", a)
    a,b = b,c
print(f"Fibonacci of {num} is {b-a}")