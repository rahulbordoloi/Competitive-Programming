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

template <typename T>
void print(vector<T>& a, char sep = ' ')
{
    for(auto i : a) { cout<<i<<sep; }
}

ll mod_opr(ll num)
{
    return (num + mod) % mod;
}

template <typename T>
bool compare(T x, T y)
{
    return x > y ? true : false;
}

// Count to Min Adjacent Swaps

std::pair<std::vector<ll>, ll> count_inversions(const std::vector<ll> &v) {

    if (v.size() == 1) return std::make_pair(std::vector<ll>(v.begin(), v.end()), 0);
    
    ll mid = (v.size()) / 2;
    
    std::vector<ll> l_half(v.begin(), v.begin() + mid);
    std::vector<ll> r_half(v.begin() + mid, v.end());
    
    auto l_ans = count_inversions(l_half);
    auto r_ans = count_inversions(r_half);
    
    std::vector<ll> mem(v.size(), 0);

    ll i{0};
    ll j{0};
    ll inv{0};
    
    for (int k = 0; k < mem.size(); ++k) {
    
        if (i < l_ans.first.size() && j < r_ans.first.size()) {
            if (l_ans.first.at(i) <= r_ans.first.at(j)) {
                mem.at(k) = l_ans.first.at(i);
                ++i;
            } else {
                mem.at(k) = r_ans.first.at(j);
                ++j;
                inv = inv + l_ans.first.size() - i;
            }
        } else if (i < l_ans.first.size()) {
            mem.at(k) = l_ans.first.at(i);
            ++i;
        } else if (j < r_ans.first.size()) {
            mem.at(k) = r_ans.first.at(j);
            ++j;
        }
    }
    
    return std::make_pair(mem, inv + l_ans.second + r_ans.second);
}
 
int main()
{
    fast;

    ll tc;
    cin>>tc;
    while(tc--){
        ll n;
        cin>>n;
        vector<ll> arr(n);
        for(auto& i : arr){
            cin>>i;
            i = (i + mod) % mod;
        }
        auto count = count_inversions(arr);
        ll x = count.second;
        if(x > (n*(n-1)/2) - 1){
            cout<<"NO";
        }
        else
            cout<<"YES";
        cout<<endl;
    }
    
    return 0;
}