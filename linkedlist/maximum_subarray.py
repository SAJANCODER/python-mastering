# ============================================================
# KADANE'S ALGORITHM - CONCEPT
# ============================================================
#
# Problem:
# Given an array, find the CONTIGUOUS (continuous) subarray
# whose sum is the maximum.
#
# Example:
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#
# Maximum Subarray = [4, -1, 2, 1]
# Maximum Sum = 6
#
# ------------------------------------------------------------
# WHY NOT CHECK EVERY SUBARRAY?
#
# We could generate all possible subarrays.
#
# Example:
# arr = [4, -1, 2]
#
# Subarrays:
# [4]
# [4, -1]
# [4, -1, 2]
# [-1]
# [-1, 2]
# [2]
#
# This takes O(n²) time.
#
# Kadane's Algorithm solves it in O(n).
# ------------------------------------------------------------


# ============================================================
# CORE IDEA
# ============================================================
#
# While moving through the array,
# keep track of the CURRENT subarray sum.
#
# At every element, ask:
#
# "Should I continue the current subarray,
#  or should I start a new one?"
#
# ------------------------------------------------------------


# Example:
#
# current_sum = -5
#
# Next element = 8
#
# Option 1:
# Continue current subarray
#
# -5 + 8 = 3
#
# Option 2:
# Start a new subarray
#
# 8
#
# Since:
#
# 8 > 3
#
# carrying the negative sum only reduces
# the future total.
#
# Therefore,
#
# discard the previous subarray
#
# current_sum = 0
#
# Then begin again from the next element.


# ============================================================
# WHY RESET current_sum TO 0?
# ============================================================
#
# A NEGATIVE running sum can NEVER help future elements.
#
# Suppose
#
# current_sum = -10
#
# Next number = 15
#
# Continue:
#
# -10 + 15 = 5
#
# Restart:
#
# 15
#
# Clearly
#
# 15 > 5
#
# Therefore,
#
# a negative running sum is useless.
#
# Reset it.
#
# if current_sum < 0:
#     current_sum = 0


# ============================================================
# WHY KEEP max_sum?
# ============================================================
#
# current_sum changes continuously.
#
# But once we find a better answer,
# we don't want to lose it.
#
# Example:
#
# Current sums become
#
# 4
# 3
# 5   <-- Best so far
# -2
# 6   <-- New Best
#
# max_sum stores the BEST answer
# seen anywhere in the array.


# ============================================================
# VARIABLES
# ============================================================
#
# current_sum
#
# -> Sum of the subarray we are currently building.
#
#
# max_sum
#
# -> Largest subarray sum found so far.


# ============================================================
# ALGORITHM
# ============================================================
arr = list(map(int,input("Enter the array:").split()))
current_sum=0
max_sum = float('-inf')
for i in arr:
    current_sum+=i
    max_sum=max(max_sum,current_sum)

    if current_sum<0:
        current_sum=0
print(max_sum)

# ============================================================
# DRY RUN
# ============================================================
#
# Array
#
# [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#
# ------------------------------------------------------------
#
# num = -2
#
# current_sum = -2
# max_sum = -2
#
# current_sum < 0
#
# Reset
#
# current_sum = 0
#
# ------------------------------------------------------------
#
# num = 1
#
# current_sum = 1
#
# max_sum = 1
#
# ------------------------------------------------------------
#
# num = -3
#
# current_sum = -2
#
# max_sum = 1
#
# Reset
#
# current_sum = 0
#
# ------------------------------------------------------------
#
# num = 4
#
# current_sum = 4
#
# max_sum = 4
#
# ------------------------------------------------------------
#
# num = -1
#
# current_sum = 3
#
# max_sum = 4
#
# ------------------------------------------------------------
#
# num = 2
#
# current_sum = 5
#
# max_sum = 5
#
# ------------------------------------------------------------
#
# num = 1
#
# current_sum = 6
#
# max_sum = 6
#
# ------------------------------------------------------------
#
# num = -5
#
# current_sum = 1
#
# max_sum = 6
#
# ------------------------------------------------------------
#
# num = 4
#
# current_sum = 5
#
# max_sum = 6
#
# Final Answer = 6
#
# Maximum Subarray = [4, -1, 2, 1]
#
# ============================================================
# INTERVIEW ONE-LINER
# ============================================================
#
# "Kadane's Algorithm keeps extending the current subarray
# while it is profitable. If the running sum becomes negative,
# it discards that subarray because a negative sum can never
# increase the sum of any future subarray."
#
# Time Complexity : O(n)
# Space Complexity: O(1)
# ============================================================