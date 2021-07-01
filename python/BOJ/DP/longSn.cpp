#include <iostream>
#include <algorithm>

using namespace std;
int A[1001];
int D[1001];

int foo(int n){
    for(int i=1; i<=n; i++){
        D[i] = 1;
        for(int j=1; j<i; j++){
            if(A[i] > A[j]){
                if(D[j] + 1 > D[i])
                    D[i] = D[j] + 1;                
            }
        }
    }
    sort(D, D+n+1);
    return D[n];
}

int main(){

    int N;
    cin >> N;
    for(int i=1; i<=N; i++){
        cin >> A[i];
    }
    cout << foo(N) << endl;
    return 0;
}