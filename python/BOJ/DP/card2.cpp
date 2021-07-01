#include <iostream>
#include <algorithm>

using namespace std;
int N;
int P[10001];
int D[10001];

int buy(int k){
    D[1] = P[1];
    
    for(int i=2; i<=k; i++){
        for(int j=1; j<=i/2; j++){
            if(D[i] >0)
                D[i] = min(D[i-j]+D[j], D[i]);
            else
                D[i] = min(D[i-j]+D[j], P[i]);
        }
    }
    return D[k];
}

int main(){
    cin >> N;

    for(int i=1; i<=N; i++){
        cin >> P[i];
    }
    cout << buy(N) << endl;
    return 0;
}