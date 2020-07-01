#include <iostream>
#include <vector>

using namespace std;
int N;
int cnt;
int c[16];

bool check(int k){
    for(int j=0; j<k; j++){
        if(c[k] == c[j] || abs(j-k) == abs(c[j]-c[k]))
            return false;
    }
    return true;
}

void queen(int index){
    if(index == N){
        cnt++;
        return ;
    }
    for(int i=0; i<N; i++){
        c[index] = i;
        if(check(index) == true){
            queen(index+1);
        }
    }
}

int main(){

    cin >> N;
    queen(0);
    cout << cnt << '\n';
    return 0;
}