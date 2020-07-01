#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

int T,N;

int main(){
    cin >> T;

    while(T--){
        
        cin >> N;
        vector<pair<int,int>> v;
        for(int i=0; i<N; i++){
            int a,b;
            cin >> a >> b;
            v.push_back(make_pair(a,b));
        }
        sort(v.begin(), v.end());
        stack<int> s;
        s.push(v[0].second);
        for(int i=1; i<N; i++){
            if(v[i].second < s.top())
                s.push(v[i].second);
        }
        cout << s.size() << endl;
    }


    return 0;
}