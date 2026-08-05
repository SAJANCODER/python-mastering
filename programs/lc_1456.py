n = input("Enter the word: ")
vowels = ['a','e','i','o','u']
k = int(input("Enter the window size: "))
total_win = len(n)-k+1
countx = float('-inf')
for i in range(total_win):
    count1 = 0
    window = n[i:k+i]
    for j in window:
        if j in vowels:
            count1+=1
    countx = max(countx,count1)
print(countx)
