#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

priority_queue <int> pq;

int main(){
    int T;
    cin >> T;
    pair <int,int> N;
    vector<pair<int,int>> v;
    for(int i=0; i<T; i++){
        int c, a, b;
        cin >> c >> a >> b;
        v.push_back(make_pair(a,b));
    }
    
    sort(v.begin(), v.end());
    pq.push(-v[0].second);

    for(int i=1; i<T; i++){
        if(-pq.top() <= v[i].first){
            pq.pop();
            pq.push(-v[i].second);
        }
        else{
            pq.push(-v[i].second);
        }
    }
    cout << pq.size() << endl;

    return 0;
}