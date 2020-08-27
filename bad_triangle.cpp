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
#define mod 100000000

using namespace std;

void print(vector<ll>& a, char sep = ' ')
{
    for(auto i : a) { cout<<i<<sep; }
}
bool compare_sides(ll a, ll b, ll c)
{
    if((a + b) > c)     return true;
    else    return false;
}

int main()
{
    int tc;
    cin>>tc;
    while(tc--)
    {
        ll n;
        cin>>n;
        vector<ll> arr(n);
        for(ll& i : arr) { cin>>i; }
        // print(arr);
        if(arr[0] + arr[1] > arr[n-1])        cout<<-1<<endl;
        else     cout<<1<<' '<<2<<' '<<n<<endl; 
    }
}