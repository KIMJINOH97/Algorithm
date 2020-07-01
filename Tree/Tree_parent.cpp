#include <iostream>
#include <vector>
#include <queue>
#define N 100001
using namespace std;

vector<int> v[N];
queue<int> q;
bool check[N];
int parent[N];

void bfs(int root){
    check[root] = true;
    q.push(root);
    while(!q.empty()){
        int x = q.front();
        q.pop();
        for(int i=0; i<v[x].size(); i++){
            if(check[v[x][i]] == false){
                check[v[x][i]] = true;
                parent[v[x][i]] = x;
                q.push(v[x][i]);
            }
        }
    }
}

int main(){

    int n, a, b;

    cin >> n;
    for(int i=1; i<n; i++){
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }  

    bfs(1);
    for(int i=2; i<=n; i++){
        cout << parent[i] << '\n';
    }

    return 0;
}