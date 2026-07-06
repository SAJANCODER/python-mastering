# In how many distinct ways can you climb to the top?
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: (1+1), (2)

# 🎯 Example 2:
# Input: n = 3
# Output: 3
# Explanation:
# 1+1+1  
# 1+2  
# 2+1  
n = int(input("Enter the stairs:"))
def staris(n,path=[]):
    if n==0:
        print(path)
        return
    if n>=1:
        staris(n-1,path+[1])
    if n>=2:
        staris(n-2,path+[2])

staris(n)    