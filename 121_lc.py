#buy sell stock
arr = list(map(int, input("Enter the array: ").split(" ")))
buy_stock = arr[0]
sell_stock = 0
for i in range(len(arr)):
    if arr[i]<buy_stock:
        buy_stock=arr[i]
    profit = arr[i]-buy_stock
    if profit>sell_stock:
        sell_stock = profit
print(sell_stock)

