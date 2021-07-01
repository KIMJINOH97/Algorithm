#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

vector<int> a[20001];
int color[20001];

void dfs(int V, int c){
    color[V] = c;
    for(int i = 0; i< a[V].size(); i++){
        int Next = a[V][i];
        if(color[Next] == 0)
            dfs(Next,3-c);
    }
}

int main(){

    int K,V,E;
    cin >> K;

    while(K--){
        cin >> V >> E;

        for(int i=1; i<=V; i++){
            a[i].clear();
            color[i] = 0;
        }

        int u,k;
        for(int i = 0; i<E; i++){
            cin >> u >> k;
            a[u].push_back(k);
            a[k].push_back(u);
        }

        for(int i = 1; i<V; i++){
            if(color[i] == 0){
                dfs(i, 1);
            }
        }

        bool check = true;

        for(int i = 1; i<=V; i++){
            for(int j = 0; j< a[i].size(); j++){
                int k=a[i][j];
                if(color[i] == color[k])
                    check = false;
            }
        }

        if(check){
            cout << "YES" << '\n';
        }
        else{
            cout << "NO" << '\n';
        }
    }


    return 0;
}