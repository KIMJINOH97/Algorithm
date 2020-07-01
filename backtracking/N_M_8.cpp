#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int N,M;
int a[10];

void go(int index, int start, vector<int> k){
    if(index == M){
        for(int j=0; j<M; j++)
            cout << a[j] << ' ';
        cout << '\n';
        return ;
    }

    for(int i=start; i<N; i++){
        a[index] = k[i];
        go(index + 1, i, k);
    }
}

int main(){
    cin >> N >> M;
    vector<int> v(N);

    for(int i=0; i<N; i++)
        cin >> v[i];

    sort(v.begin(), v.end());
    go(0, 0, v);

    return 0;
}