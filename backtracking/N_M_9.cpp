#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int N,M;
int a[10];
int num[10];
int cnt[10];

void go(int index, vector<int> k){
    if(index == M){
        for(int j=0; j<M; j++)
            cout << a[j] << ' ';
        cout << '\n';
        return ;
    }
    for(int i=0; i<N; i++){
        if(cnt[i]>0){
            cnt[i] -= 1;
            a[index] = num[i];
            go(index+1, k);
            cnt[i] += 1;
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
    int temp = v[0];
    int count = 1;
    int k=0;
    for(int i=1; i<N; i++){
        if(temp == v[i]){
            count+=1;
        }
        else{
            num[k] = temp;
            cnt[k] = count;
            k++;
            temp = v[i];
            count = 1;
        }
    }
    num[k] = temp;
    cnt[k] = count;
    go(0, v);

    return 0;
}