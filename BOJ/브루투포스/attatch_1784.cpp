#include <iostream>

using namespace std;

int main(){
    int N;
    cin >> N;
    int sum = 0;
    for(int i=1; i<=N; i++){
        int cnt = 0;
        for(int j=i; j>0; j/=10){
            cnt++;
        }
        sum += cnt;
    }
    cout << sum << endl;
    return 0;
}