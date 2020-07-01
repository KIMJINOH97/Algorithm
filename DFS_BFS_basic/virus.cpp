#include <iostream>
#include <vector>

using namespace std;

int count =0;
vector<int> v[101];
bool infect[101];

void dfs(int start){
    infect[start] = true;
    for(int i = 0; i<v[start].size(); i++){
        int next = v[start][i];
        if(infect[next] == false){
            infect[next] = true;
            count++;
            dfs(next);
        }
    }
}

int main(){

    int N, E;
    cin >> N >> E;

    for(int i = 0; i<E; i++)
    {
        int a,b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }

    dfs(1);  
    cout << count << endl;  

    return 0;
}