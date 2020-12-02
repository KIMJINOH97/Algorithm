#include <iostream>
#include <algorithm>

using namespace std;

int c[101];
int dp[10001][101];
int a[10001];

int main(){
    int n,k;
    cin >> n >> k;
    for(int i=1; i<=n; i++){
        int a;
        cin >> a;
        c[i] = a;
    }
    sort(c+1, c+n+1);
    
    for(int i=1; i<=k; i++){
        dp[c[i]][i] = 1;
        for(int j=1; j<=n; j++){
            for(int l=1; l<=n; l++){
                if(i-c[j] >0)
                    dp[i][j] += dp[i-c[j]][l];
            }
        }
    }
    int res=0;
    for(int i=1; i<=k; i++){
        //res += dp[k][i];
        for(int j=1; j<=n; j++){
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }
    //cout << res << endl;
    return 0;
}