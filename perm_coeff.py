def perm(n,k):
    fn=1
    for i in range(1,n+1):
        fn*=i
        if (i == n-k):
            fk=fn
    coeff=fn//fk
    print(coeff)

def main():
    n,k=map(int,input().split())
    perm(n,k)

if __name__=='__main__':
    main()