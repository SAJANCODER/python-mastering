a=int(input("enter a number:"))
prime=True
for i in range(2,a):
    if a%i==0:
        prime=False
    else:
        break
if prime:
    print("prime number")
else:
    print("not a prime number")

#a prime number is a number that has two positive divisors , that is
    #it can be divisible by 1 and the divisible by the excat same number(itself).
