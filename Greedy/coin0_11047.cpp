#include <iostream>
#include <vector>

using namespace std;
int N,K;
vector<int> v;
void gd(){
    int cnt =0;
    bool escape = false;
    while(1){
        for(int i=N-1; i>=0; i--){
            if(K-v[i] >= 0){
                K -= v[i];
                cnt++;
                if(K==0)
                    escape = true;
                break;    
            }
        }
        if(escape == true)
            break;
    }
    cout << cnt << endl;
}

int main(){
    cin >> N >> K;
    for(int i=0; i<N; i++){
        int a;
        cin >> a;
        v.push_back(a);
    }

    gd();
    return 0;
}