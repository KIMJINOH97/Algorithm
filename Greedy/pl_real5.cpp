#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>

using namespace std;
int N;
vector<pair<int,int>> v;
stack<pair<int,int>> s;
void foo(){
    s.push(make_pair(v[0].first, v[0].second));
    for(int i=1; i<N; i++){
        if(v[i].first >= s.top().second){
            s.push(make_pair(v[i].first, v[i].second));
        }
        else if(v[i].second < s.top().second){
            s.pop();
            s.push(make_pair(v[i].first, v[i].second));
        }
    }  
    cout << s.size() << endl; 
}

int main(){
    cin >> N;
    for(int i=0; i<N; i++){
        int a,b;
        cin >> a >> b;
        v.push_back(make_pair(a,b));
    }
    sort(v.begin(), v.end());

    foo();
    return 0;
}
