#include <iostream>
#include <stack>
using namespace std;
int N;
int A[1001];
int D[1001][2];
stack<int> s;
void dp(int n){
    for(int i=0; i<n; i++){
        D[i][0] = 1;
        D[i][1] = -1;
        for(int j=0; j<i; j++){
            if(A[j] < A[i] && D[j][0]+1 > D[i][0]){
                D[i][0] = D[j][0] + 1;
                D[i][1] = j;
            }
        }
    }
    int max = -1;
    for(int i=0; i<n;i++){
        if(D[i][0] > max){
            max = D[i][0];
        }
    }
    int cnt = 0;
    for(int i=0; i<n; i++){
        if(D[i][0] == max){
            cnt = i;
            break;
        }
    }
    s.push(A[cnt]);
    while(1){
        if(D[cnt][1] == -1)
            break;
        s.push(A[D[cnt][1]]);
        cnt = D[cnt][1];
    }
    cout << max << endl;

    while(!s.empty()){
        cout << s.top() << ' ';
        s.pop();
    }
    return ;
}

int main(){
    cin >> N;
    for(int i=0; i<N; i++)
        cin >> A[i];
    dp(N);    
    return 0;
}