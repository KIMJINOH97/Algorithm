#include <iostream>
#define N 100001
using namespace std;
long long D[N][4];

long long foo(int k){
    
    for(int i=4; i<=k; i++){
        if(D[i][1] == 0){
            D[i][1] = (D[i-1][2]%1000000009+D[i-1][3]%1000000009)%1000000009;
            D[i][2] = (D[i-2][1]%1000000009+D[i-2][3]%1000000009)%1000000009;
            D[i][3] = (D[i-3][1]%1000000009+D[i-3][2]%1000000009)%1000000009;
        }
    }
    return (D[k][1]+D[k][2]+D[k][3])%1000000009;
}

int main(){
    D[1][1] = 1;
    D[2][2] = 1;
    D[3][3] = 1;
    D[3][2] = 1;
    D[3][1] = 1;

    int T,n;
    cin >> T;
    while(T--){
        cin >> n;
        cout << foo(n) << endl;
    }
    return 0;
}