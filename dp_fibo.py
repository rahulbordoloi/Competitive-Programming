"""#recusion
def fibo(n):
    if n==1 or n==2:
        result=1
    else:
        result= fibo(n-1) + fibo(n-2)
    return result"""

#memoization
def fibo_mem(n,memo):                   #filling the array from L->R as we go on traversing
    if memo[n] is not None:
        return memo[n]
    if n==1 or n==2:
        result = 1
    else:
        result = fibo_mem(n-1, memo) + fibo_mem(n-2, memo)
    memo[n]=result
    return result

#bottom_up
def fibo_bottomup(n):
    if n==1 or n==2:
        result=1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):         #from 3rd element to last
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

if __name__=='__main__':
    n=int(input())
    memo = [None] * (n+1)               #always the memo list created will be n+1
    #print(fibo(8))
    print(fibo_mem(6,memo))
    #print(fibo_bottomup(8))