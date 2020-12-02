#include <iostream>

using namespace std;
int a[10];
int c[10];
void go(int index, int n, int m){
    if(index == m){
        bool ok = true;
        for(int i=0; i<m-1; i++){
            if(a[i+1] < a[i])
                ok = false;
        }
        if(ok == true){
            for(int i=0; i<m; i++){
                cout << a[i] << ' ';
        }
        cout << '\n';
        }
        return ;
    }
    for(int i=1; i<=n; i++){
        if(c[i] == true)
            continue;
        if(c[i] == false){
            c[i] = true;
            a[index] = i;
            go(index+1, n, m);
            c[i] = false;
        }
    }
}

int main(){
    int N,M;

    cin >> N >> M;
    go(0, N, M);

    return 0;
}