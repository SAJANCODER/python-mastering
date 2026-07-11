arr = list(map(int,input("Enter the array:").split()))
window = 3
maxi = 0
n = sum(arr[:window])
for i in range(window,len(arr)):
    total = n+arr[i]-arr[i-window]
    n=total
    maxi=max(maxi,total)

print(maxi)