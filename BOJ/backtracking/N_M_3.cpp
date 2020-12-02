#include <iostream>

using namespace std;
int a[10];

void go(int index, int n, int m){
    if(index == m){
        for(int j=0; j<m; j++)
            cout << a[j] << ' ';
        cout << '\n';
        return ;
    }

    for(int i=1; i<=n; i++){
        a[index] = i;
        go(index+1, n, m);
    }
}

int main(){
    int N,M;
    cin >> N >> M;
    go(0, N, M);

    return 0;
}