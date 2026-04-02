a=int(input("enter a number:"))
prime=True
for i in range(2,a):
    if a%i==0: #it stops at the first step itself . make sure modulus is the reminder of division . like 6%3 = 3*2 = 6 right reminder =0 . failed here .
        # modulus is reminder = 6%4 = 1*6=6 , then 6-4 = 2 . so the reminder is 2 . therefore 6%4 = 2
        #then why 4%6 = 4 . Whenever the first number is smaller, remainder = the first number.
        prime=False
        break
if prime:
    print("prime number")
else:
    print("not a prime number")

#a prime number is a number that has two positive divisors , that is
    #it can be divisible by 1 and the divisible by the excat same number(itself).


