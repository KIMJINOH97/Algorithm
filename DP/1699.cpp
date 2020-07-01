#include <iostream>
#include <cmath>
using namespace std;
int d[100001];
int a[100001];
int dp(int N){
    d[1] = 1;
    for(int i=2; i<=N; i++){
        int min = 100000;
        for(int j=sqrt(i); j>0; j--){
            if(j*j == i){
                min = 1;
                break;
            }
            else{
                a[j] = d[i-j*j] + 1;
                if(a[j] < min){
                    min = a[j];
                }
            }
        }
        d[i] = min;
    }
    return d[N];
}

int main(){
    int N;
    cin >> N;
    cout << dp(N) << endl;

    return 0;
}