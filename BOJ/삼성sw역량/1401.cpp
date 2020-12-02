#include <bits/stdc++.h>

using namespace std;
vector<int> profit;
int T[16]; int P[16]; int c[16];
int N;
queue<pair<int, int>> q;
void bfs(int day){
    q.push({day, P[day]});
    while(!q.empty()){
        int d = q.front().first;
        int p = q.front().second;
        if(d == N && T[d] == 1 || d+T[d]==N+1){
            profit.push_back(p);
        }
        q.pop();
        for(int i=d+T[d]; i<=N; i++){
            if(i + T[i] > N+1){
                profit.push_back(p);
                continue;
            }
            q.push({i, p+P[i]});
        }
    }
}

int main(){
    cin >> N;
    for(int i=1; i<=N; i++){
        cin >> T[i] >> P[i];
    }
    int Max_profit = 0;
    for(int i=1; i<=N; i++){
        bfs(i);
    }

    if(profit.size() != 0)
        Max_profit = *max_element(profit.begin(), profit.end());
    cout << Max_profit << endl;

    return 0;
}