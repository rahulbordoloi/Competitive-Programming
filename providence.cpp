#include <bits/stdc++.h>

#define fast ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL)
#define f(i,a,b) for(i=a;i<b;i++)
#define fi(i,a,b,x) for(i=a;i<b;i=i+x)
#define fe(i,a,b) for(i=a;i<=b;i++)
#define fr(i,a,b) for(i=a;i>=b;i--)
#define endl '\n'
#define sp '\t'
#define ll long long int
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define mod 1000000007

using namespace std;

vector<vector <ll> > answers;
int i = 0;

void print(vector<vector <ll> > a)
{
    for(auto i : a){
        cout<<i[0]<<" "<<i[1]<<endl;
    }
}

/*
void print(vector<ll> a, char sep)
{
    for(auto i : a) { cout<<i<<sep; }
}
*/

ll mod_opr(ll num)
{
    return (num + mod) % mod;
}

bool compare(ll x, ll y)
{
    return x > y ? true : false;
}

int main()
{
    fast;
    ll tc,n;
    cin>>tc;
    ll a,b,c;
    while(tc--){
        cin>>a>>b>>n;
        n--;
        while(n--){
            c = a;
            a = (b - a + mod) % mod;
            b = (c + b) % mod;
        }
        // cout<<a<<" "<<b<<endl;
        answers.pb(vector<ll> {a,b});
    }
    print(answers);

    return 0;
}