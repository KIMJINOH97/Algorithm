#include <iostream>
#define n 1000000000
using namespace std;
int N, K;
int d[201][201];
int dp(int N, int K){
    for(int i=0; i<=200; i++){
        d[0][i] = 1;
        d[i][1] = 1;
    }

    for(int i=1; i<=200; i++){
        for(int j=2; j<=200; j++){
            for(int k=0; k<=i; k++){
                d[i][j] += d[i-k][j-1]%n;
                d[i][j] = d[i][j]%n;
            }
        }
    }

    return d[N][K];
}

int main(){
    cin >> N >> K;
    cout << dp(N, K) << endl;
    return 0;
}