arr = list(map(int,input("Enter the array number: ").split(" ")))
prime_no = []
non_prime = []

for i in arr:
    factor = 0
    for j in range(1,i+1):
        if i%j==0:
            factor+=1
    if factor==2:
        prime_no.append(i)
    else:
        non_prime.append(i)
prime_no = sorted(prime_no)
non_prime = sorted(non_prime,reverse=True)

p=0
np=0
final_arr = []
for i in range(len(arr)):
    if arr[i] in prime_no:
        final_arr.append(prime_no[p])
        p+=1
    else:
        final_arr.append(non_prime[np])
        np+=1
print(final_arr)