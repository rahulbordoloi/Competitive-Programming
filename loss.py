mod = 1000000007
n = int(input())    # Number of Years of House Data
n %= mod
price = [int(i) for i in input().split()]
price = [i % mod for i in price]
# print(*price)
price.sort()
# print(price[1] - price[0])
diff = 10 ** 20
for i in range(n - 1):
    if price[i + 1] - price[i] < diff:
        diff = price[i + 1] - price[i]
print(diff)
del n, price, diff