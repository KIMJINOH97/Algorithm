#include <iostream>
#include <algorithm>

using namespace std;
int N,M;
int a[10];
int num[10];
int temp[10];

void go(int index){
    if(index == M){
        for(int i=0; i<M; i++)
            cout << a[i] << ' ';
        cout << '\n';
        return ;
    }
    for(int j=0; j<N; j++){
        if(num[j]>0){
            a[index] = num[j];
            go(index+1);
        }
    }
}

int main(){
    cin >> N >> M;

    for(int i=0; i<N; i++)
        cin >> temp[i];
    sort(temp, temp+N);
    int a = temp[0];
    int k=0;
    for(int i=1; i<N; i++){
        if(a != temp[i]){
            num[k] = a;
            a = temp[i];
            k++;
        }
    }
    num[k] = a;

    go(0);

    return 0;
}