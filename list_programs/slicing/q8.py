#Take a string input and rotate its characters to the right by 2 positions.
#Example: "hello" → "lohel"

string = input("Enter the String: ")
rotate = string[-2:] + string[:-2]
print(f"Reverse Text: {rotate}")