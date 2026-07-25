n = int(input("Enter the value:"))
x=0
for i in range(1,n+1):
    x = n-i
    print(x*" ",end="")
    for j in range(2*i-1):
        print("#",end="")
    print()


# This is the most important question in pattern printing. Don't memorize 2*i - 1; understand why it appears.

# Let's build it from scratch.

# Suppose you want this pyramid:

#     #
#    ###
#   #####
#  #######
# #########

# Now count the stars in each row:

# Row (i)	Stars
# 1	        1
# 2	        3
# 3	        5
# 4	        7
# 5	        9

# Look at the sequence:

# 1, 3, 5, 7, 9

# What do you notice?

# Every row adds 2 more stars than the previous one.

# 1 + 2 = 3
# 3 + 2 = 5
# 5 + 2 = 7
# 7 + 2 = 9

# This is the sequence of odd numbers.

# How do we generate odd numbers?

# Let's write the row number (i) and calculate 2*i:

# i	2*i
# 1	2
# 2	4
# 3	6
# 4	8
# 5	10

# These are even numbers.

# But we need:

# 1, 3, 5, 7, 9

# So subtract 1:

# i	2*i	2*i - 1
# 1	2	1 ✅
# 2	4	3 ✅
# 3	6	5 ✅
# 4	8	7 ✅
# 5	10	9 ✅

# That's exactly the number of stars needed.