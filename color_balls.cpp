# include <bits/stdc++.h>

#define fast ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL)
#define f(i,a,b) for(i=a;i<b;i++)
#define fi(i,a,b,c) for(i=a;i<b;i=i+c)
#define fr(i,a,b) for(i=a;i>=b;i--)
#define endl '\n'
#define ll long long int
#define ff first
#define ss second
#define pb(x) push_back(x)
#define mp make_pair
#define mod 1000000007

using namespace std;

void print(vector<ll>& a, char sep = ' ')
{
    for(auto i : a) { cout<<i<<sep; }
}

int main()
{
    int tc;
    cin>>tc;
    while(tc--)
    {
        ll r,g,b,w;
        cin>>r>>g>>b>>w;
        r%=mod;g%=mod;b%=mod;w%=mod;
        ll w_count = (r%2 == 0 ? 1:0) + (g%2 == 0 ? 1:0) + (b%2 == 0 ? 1:0) + (w%2 == 0 ? 1:0);
		if(w_count > 2) cout<<"Yes"<<endl;
		else if(r == 0 || g == 0 || b == 0 || w_count == 2)     cout<<"No"<<endl;
		else cout<<"Yes"<<endl;
    }
}