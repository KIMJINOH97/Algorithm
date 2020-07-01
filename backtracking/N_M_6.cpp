#include <iostream>
#include <algorithm>

using namespace std;
int N,M;
int a[10];
int v[10];
int c[10];
void go(int index, int start){
    if(index == M){
        for(int j=0; j<M; j++)
            cout << a[j] << ' ';
        cout << '\n';
        return ;
    }
    for(int i=start; i<N; i++){
        if(c[i] == false){
            c[i] = true;
            a[index] = v[i];
            go(index+1, i);
            c[i] = false;
        }
    }
}

int main(){

    cin >> N >> M;
    
    for(int i=0; i<N; i++){
        cin >> v[i];
    }
    sort(v, v+N);
    go(0,0);

    return 0; 
}