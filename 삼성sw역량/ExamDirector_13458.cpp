#include <bits/stdc++.h>

using namespace std;

int main(){
    int N, B, C;
    cin >> N; // 시험장 수
    vector<int> A(N), director(N);
    for(int i=0; i<N; i++){
        cin >> A[i];
    }

    cin >> B >> C;

    long long sum = 0;
    
    sort(A.begin(), A.end());
    for(int i=0; i<N; i++){
        int s = A[i];
        if(i>0){
            s = s - (B+C*(director[i-1]-1));
            director[i] = director[i-1];
        }
        else{
            s = s - B;
            director[i]++;
        }
        if(s <= 0){
            sum += director[i];
            continue;
        }
        else{
            while(s>0){
                s = s-C;
                director[i]++;
            }
            sum += director[i];
        }  
        
    }
    cout << sum << endl;
    return 0;
}