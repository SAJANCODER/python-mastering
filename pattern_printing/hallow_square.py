n = int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n:
            print("*",end="")
        else:
            if j==1 or j==n:
                print("*",end="")
            else:
                print(" ",end="")
    
    print()

# The top and bottom rows are correct, but now think about the middle rows.

# Right now you have:

# if i == 1 or i == n:
#     print("*", end="")
# else:
#     ...

# The question is:

# What should happen when i is neither the first nor the last row?

# For example, when n = 5 and you're on:

# i = 2

# the output should be:

# *   *

# Now look at the columns (j).

# Since you used:

# for j in range(n):

# j will be:

# 0 1 2 3 4

# Ask yourself:

# j	Print
# 0	*
# 1	
# 2	
# 3	
# 4	*
# Your next challenge

# Inside the else: block, write a condition that checks:

# Is this the first column (j == 0)?
# Is this the last column (j == n - 1)?

# If yes, print "*".

# Otherwise, print a space " ".