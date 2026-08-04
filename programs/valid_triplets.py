n = int(input("Enter the value of n:"))
count = 0
arr=[]
for a in range(n+1):
    for b in range(n+1):
        for c in range(n+1):
            if a*a + b*b + c*c + a*b + b*c + c*a == n:
                page = []
                page.append(a)
                page.append(b)
                page.append(c)
            
                if sorted(page) not in arr:
                    arr.append(sorted(page))
                    count+=1
                
print(count)