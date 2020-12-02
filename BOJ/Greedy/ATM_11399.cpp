#include <iostream>
#include <algorithm>

using namespace std;
int P[1001];
int S[1001];
int main(){
    int N;
    cin >> N;
    for(int i=1; i<=N; i++){
        cin >> P[i];
    }
    sort(P+1, P+N+1);
    S[1] = P[1];
    int sum = S[1];
    for(int i=2; i<=N; i++){
        S[i] = S[i-1]+P[i];
        sum += S[i];
    }
    cout << sum << endl;
    return 0;
}