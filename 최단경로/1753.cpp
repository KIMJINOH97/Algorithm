#include <iostream>
#include <vector>
#include <queue>

using namespace std;
struct Node{
    int end;
    int val;
};

priority_queue<pair<int,int>> pq;
vector<Node> arr[20001];
int dist[20001];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int V,E,S;
    cin >> V >> E;
    cin >> S;
    
    for(int i=0; i<E; i++){
        int a,b,w;
        cin >> a >> b >> w;
        arr[a].push_back(Node{b,w});
    }

    for(int i=1; i<=V; i++){
        dist[i] = 999999;
    }

    dist[S] = 0;
    pq.push({0, S});

    while(!pq.empty()){
        int now = pq.top().second;
        pq.pop();

        for(int j=0; j<arr[now].size(); j++){
            int new_v = dist[now] + arr[now][j].val;
            int before_v = dist[arr[now][j].end];
            if(new_v < before_v){
                dist[arr[now][j].end] = new_v;
                pq.push({-new_v, arr[now][j].end});
            }
        }    
    }

    for(int i=1; i<=V; i++){
        if(dist[i] == 999999)
            cout << "INF" << '\n';
        else
            cout << dist[i] << '\n';
    }
    return 0;
}