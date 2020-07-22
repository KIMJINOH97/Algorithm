#include <bits/stdc++.h>

using namespace std;
vector<int> profit;
int T[16]; int P[16]; int c[16];
int N;

int main(){
    cin >> N;
    for(int i=1; i<=N; i++){
        cin >> T[i] >> P[i];
    }

    for(int i=1; i<=N; i++){
        cout << T[i] << " " << P[i] << endl;
    }
}