#anagram , rearraning the words or letters to form different word
stra = "listen"
stra2 = "stenli"
print("YES IT IS ANAGRAM" if sorted(stra) == sorted(stra2) else "NOT AN ANAGRAM")
