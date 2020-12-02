#include <iostream>
#include <cstring>

using namespace std;
int a[10];
int check[10];

void foo(int index, int n, int m){
        if(index == m){
            for(int j=0; j<m; j++){
                cout << a[j] << ' ';
            }
            cout << '\n';
            index = 0;
            return ;
        }
    for(int i=1; i<=n; i++){
        if(check[i])
            continue;
        if(check[i] == false){
            check[i] = true;
            a[index] = i;
            foo(index+1, n, m);
            check[i] = false;
        }
    }
}

int main(){

    int N, M;

    cin >> N >> M;
    foo(0, N, M);

    return 0;
}