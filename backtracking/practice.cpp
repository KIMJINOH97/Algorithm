#include <iostream>
#include <vector>

using namespace std;

int main(){
    int N;

    vector<int> v(N);
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> v[i];
    }

    for(int j=0; j<N; j++){
        cout << v[j] << ' ';
    }

    return 0;
}