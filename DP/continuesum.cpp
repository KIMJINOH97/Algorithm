#include <iostream>
#include <algorithm>
#define N 100001
using namespace std;
int n;
int D[N];
int A[N];

int main(){
    cin >> n;
    for(int i=0; i<n; i++)
        cin >> A[i];
    for(int j=0; j<n; j++){
        D[j] = max(A[j], D[j-1]+A[j]);
    }
    cout << *max_element(D,D+n) << endl;

    return 0;
}