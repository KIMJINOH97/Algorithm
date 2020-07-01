#include <iostream>
int a[10];

using namespace std;
void go(int index, int start, int n, int m){
    if(index == m){
        for(int j=0; j<m; j++)
            cout << a[j] << ' ';
        cout << '\n';
        return ;
    }

    for(int i=start-1; i<=n; i++){
        if(i>0){
            a[index] = i;
            go(index+1, i+1, n, m);
        }
    }
}

int main(){
    int N, M;

    cin >> N >> M;
    go(0, 0, N, M);

    return 0;
}