#Take a string input and rotate its characters to the right by 2 positions.
#Example: "hello" → "lohel"

num = input("Enter the string:")
rotate = num[-2:] + num[:3]
#           lo + hel
print(rotate)

