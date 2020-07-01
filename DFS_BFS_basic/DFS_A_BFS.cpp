#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <queue>
#include <stack>

using namespace std;
vector<int> v[1001];
stack<int> s;
queue<int> q;
bool check[1001];
int p[1001];

void print_stack(){
    int count = -1;
    while(!s.empty()){
        p[++count] = s.top();
        s.pop();
    }

    for(int i=count; i>=0;i--){
        cout << p[i] << " ";
    }
    cout<<'\n';
}

void bfs(int start){
    check[start] = true;
    q.push(start);
    s.push(start);
    while(!q.empty()){
        int next = q.front();
        q.pop();
        for(int i = 0; i<v[next].size(); i++){
            int k = v[next][i];
            if(check[k]==false){
                q.push(k);
                s.push(k);
                check[k] = true;
            }
        }
    }
}

void dfs(int start){
    check[start] = true;
    
    for(int i = 0; i<v[start].size(); i++){
        int next = v[start][i];
        if(check[next] == false){
            check[next] = true;
            s.push(next);
            dfs(next);
        }
    }   
}

int main(){

    int N, M, V;
    cin >> N >> M >> V;
    for(int i =0; i<M; i++){
        int a,b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }

    for(int i = 0; i< 1001; i++){
        sort(v[i].begin(), v[i].end());
    }
    s.push(V);
    dfs(V);
    print_stack(); 
    memset(check,false,sizeof(check));
    bfs(V);
    print_stack();
    return 0;
}