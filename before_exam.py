d, sumT = map(int, input().split())
minT = []
maxT = []
for i in range(d):
    x, y = map(int, input().split())
    minT.append(x)
    maxT.append(y)

tempS = sumT - sum(minT)
if tempS < 0:       print("NO")
if tempS == 0:
    print("YES")


'''
int t,i,j,k,d,sum,a[1000],b[1000];
	while(~scanf("%d%d",&d,&sum))
	{
		for(i = 1 ; i <= d ; i++)
		{
			scanf("%d%d",&a[i],&b[i]);
			sum -= a[i];
		}
		if(sum < 0)
		{
			printf("NO\n");
				continue;
		}
		else if(sum == 0)
		{
			printf("YES\n");
			for(i = 1 ; i<= d ;i++)
			{
				printf("%d ",a[i]);
			}
			printf("\n");
			continue;
		}
		for(i = 1 ; i <= d ; i++ )
		{
			t = sum;
			sum-=(b[i]-a[i]);
			if(sum <= 0)
				break;
		}
		if(sum > 0)
		{
			printf("NO\n");
			continue;
		}
		printf("YES\n");
		for(j = 1 ; j <= d ; j++)
		{
			if(j < i )
			printf("%d ",b[j]);
			else if( j == i)
				printf("%d ",a[j] + t);
			else
				printf("%d ",a[j]);
		}
		printf("\n");
	}
	return 0;
}
'''