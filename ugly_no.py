"""Ugly Numbers 
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. 
By convention, 1 is included.
Given a number n, the task is to find n’th Ugly number."""

def ugly_no(n):
    ugly=[0]*n
    ugly[0]=1
    mul_2,mul_3,mul_5=2,3,5
    x=y=z=0                              #indices for 2,3,5
    for i in range(1,n):
        ugly[i]=min(mul_2,mul_3,mul_5)
        if ugly[i] == mul_2:
            x+=1
            mul_2 = ugly[x] * 2
        if ugly[i] == mul_3:
            y+=1
            mul_3 = ugly[y] * 3
        if ugly[i] == mul_5:
            z+=1
            mul_5 = ugly[z] * 5
    print(*ugly)
    #print(ugly[-1])

def main():
    n=10
    ugly_no(n)

if __name__=='__main__':
    main()
