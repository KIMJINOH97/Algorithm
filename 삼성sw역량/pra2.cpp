#include <bits/stdc++.h>

using namespace std;
vector<int> profit;
int T[16]; int P[16]; int c[16];
int N;
vector<pair<int,int>> v(4);
void route_left(){
    int a = v[3].first;
    int b = v[3].second;
    v[3] = v[2];
    v[2] = v[1];
    v[1] = v[0];
    v[0].first = a;
    v[0].second = b;
}

int main(){
    v = {{-1,0}, {0,1}, {0,1}, {0,-1}};
    route_left();

    cout <<v[0].first << ' ' << v[0].second << endl;

    return 0;
}