#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int N,M;
int a[10];
int c[10];
void go(int index, vector<int> vec){
    if(index == M){
        for(int j=0; j<M; j++)
            cout << a[j] << ' ';
        cout << '\n';
        return ;
    }
    for(int i=1; i<=N; i++){
        if(c[i] == false){
            a[index] = vec[i-1];
            c[i] = true;
            go(index+1, vec);
            c[i] = false;
        }
    }
}

int main(){
    cin >> N >> M;
    vector<int> v(N);
    for(int i=0; i<N; i++){
        cin >> v[i];
    }
    
    sort(v.begin(), v.end());
    go(0, v);

    return 0;
}