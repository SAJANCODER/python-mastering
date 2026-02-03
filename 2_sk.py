#n = int(input("Enter a number:"))
#count = 0
#while True:
 #   count +=len(str(n))
#print(count)
# the above method is brute force


n = int(input())
start =1
digits =1
count =0
while start*10<=n:
    count+= (start*9)*digits
    start*=10
    digits+=1
count += (n-start+1)*digits
print(count)
