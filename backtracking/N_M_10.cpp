#include <iostream>
#include <algorithm>

using namespace std;
int N,M;
int a[10];
int temp[10];
int num[10];
int cnt[10];

void go(int index, int start){
    if(index == M){
        for(int i=0; i<M; i++)
            cout << a[i] << ' ';
        cout << '\n';
        return ;
    }
    for(int j=start; j<N; j++){
        if(cnt[j] >0){
            cnt[j] -=1;
            a[index] = num[j];
            go(index+1, j);
            cnt[j] +=1;
        }
    }
}

int main(){
    cin >> N >> M;
    for(int i=0; i<N; i++)
        cin >> temp[i];
    sort(temp, temp+N);
    int k=0;
    int count = 1;
    int a = temp[0];
    for(int i=1; i<N; i++){
        if(a == temp[i]){
            count++;
        }
        else{
            cnt[k] = count;
            num[k] = a;
            a = temp[i];
            k++;
            count = 1;
        }
    }
    cnt[k] = count;
    num[k] = a;

    go(0, 0);

    return 0;
}