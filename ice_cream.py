tc = int(input())
mod = 1000000007
while tc:
    m = int(input())                       # Amount of money they have pooled
    m %= mod
    n = int(input())                       # Number of flavors offered at the time
    n %= mod
    cost = list(map(int, input().split())) # Cost of Each Flavour
    cost = [i % mod for i in cost]
    ans = []
    for i in range(len(cost)):
        if m >= cost[i]:
            m -= cost[i]
            ans.append(i + 1)
    print(*ans)
    del m, n, cost, ans
    tc -= 1
del tc