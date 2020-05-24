"""Coin Change
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, 
how many ways can we make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. 
For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5."""

#Method 1
def count(S,m,n): 
    table=[0 for k in range(n+1)] 
    table[0]=1                        #Base case (If given value is 0) 
    for i in range(0,m):              #Pick all coins one by one and update the table[] values after the index greater than or equal to the value of the picked coin
        for j in range(S[i],n+1): 
            table[j] += table[j-S[i]] 
            #print("\tIteration:");print("\tj,S[i]=\t"+str(j)+str(S[i]));print(*table)
        #print("\n")
    #print(*table)
    return table[n] 

def main():
    n=int(input())         #change no
    a=[1,2,3]              #coins
    m=len(a) 
    x=count(a,m,n) 
    print(x) 

if __name__=='__main__':
    main()

#Method 2
"""def count(S, m, n): 
    table = [[0 for x in range(m)] for x in range(n+1)] 
    # Fill the entries for 0 value case (n = 0) 
    for i in range(m): 
        table[0][i] = 1
    # Fill rest of the table entries in bottom up manner 
    for i in range(1, n+1): 
        for j in range(m): 
            # Count of solutions including S[j] 
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
            # Count of solutions excluding S[j] 
            y = table[i][j-1] if j >= 1 else 0
            # total count 
            table[i][j] = x + y 
    print(*table)
    return table[n][m-1] 
arr = [1, 2, 3] 
m = len(arr) 
n = 4
print(count(arr, m, n))"""

