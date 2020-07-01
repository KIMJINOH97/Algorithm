#include <iostream>

using namespace std;
int N;
int a[8];
int bs(int l, int r){
    int mid = (l+r)/2;
    while(l<r){
        int mid = (l+r)/2;
        if(N == a[mid])
            return mid;
        if(N < a[mid]){
            r = mid-1;
        }
        else{
            l = mid+1;
        }
    }
    return -1;
}

int main(){
    for(int i=0; i<8; i++)
        cin >> a[i];
    cin >> N;
    int ans = bs(0,7);
    if(ans == -1)
        cout << "There is no answer" << endl;
    else
        cout << ans+1 << endl;
    return 0;
}