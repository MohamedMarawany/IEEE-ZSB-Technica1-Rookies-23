#include <bits/stdc++.h>
 
using namespace std;
 
void solve(){
    long long n,t;
    cin >> n >> t;
    long long a[n];
    for (int i=0; i<n; i++){
        cin >> a[i];
    }
    long long sum = 0;
    long long res = 0;
    for(int i=0; i<n; i++){
        if(sum < t){
            res++;
        sum += 86400 - a[i];
        }
    }
    cout << res << endl;
}
 
int main(){
    int t=1;
    while(t--){
      solve();  
    } 
}
