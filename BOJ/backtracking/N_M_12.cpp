#include <iostream>
#include <algorithm>

using namespace std;
int N,M;
int a[10];
int temp[10];
int num[10];

void go(int index, int start){
    if(index == M){
        for(int i=0; i<M; i++)
            cout << a[i] << ' ';
        cout << '\n';
        return ;
    }
    for(int j=start; j<N; j++){
        if(num[j] >0){
            a[index] = num[j];
            go(index+1, j);
        }
    }
}

int main(){
    cin >> N >> M;
    for(int i=0; i<N; i++){
        cin >> temp[i];
    }
    sort(temp, temp+N);
    int k=0;
    int t = temp[0];
    for(int i=1; i<N; i++){
        if(t !=temp[i]){
            num[k] = t;
            t = temp[i];
            k++;
        }
    }
    num[k] = t;

    go(0, 0);
    return 0;
}