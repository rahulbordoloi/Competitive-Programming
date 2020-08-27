# include <bits/stdc++.h>

#define fast ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL)
#define f(i,a,b) for(i=a;i<b;i++)
#define fi(i,a,b,c) for(i=a;i<b;i=i+c)
#define fr(i,a,b) for(i=a;i>=b;i--)
#define endl '\n'
#define ll long long int
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define mod 1000000007

using namespace std;

void print(vector<ll>& a, char sep = ' ')
{
    for(auto i : a) { cout<<i<<sep; }
}

int main()
{
    ll n,m,x,y;
    cin>>n>>m>>x>>y;
    for(ll i=1; i<=m; i++)
    {
        for (ll j=1; j<=n; j++)
        {
            cout<<x<<" "<<y<<endl;
            if(j!=n)    x = x % n + 1;
        }
        if(i!=m)    y = y % m + 1;
    }
    return 0;
}


