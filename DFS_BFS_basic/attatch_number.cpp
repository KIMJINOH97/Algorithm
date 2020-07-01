#include <iostream>
#include <cstdio>
#include <algorithm>
#include <tuple>
#include <queue>

using namespace std;

int a[26][26];
int d[26][26];
queue<pair<int,int>> q;
int N = 0;
int nx[] = {0,0,1,-1};
int ny[] = {1,-1,0,0};

void bfs(int x, int y, int cnt)
{
    q.push(make_pair(x,y));
    a[x][y] = cnt;
    while(!q.empty())
    {
        tie(x,y) = q.front();
        q.pop();
        for(int k=0; k<4; k++){
            int dx = x + nx[k];
            int dy = y + ny[k];
        
                if(dx >=0 && dx < N && dy >=0 && dy < N){
                if(a[dx][dy] == 0 && d[dx][dy] == 1){
                    q.push(make_pair(dx,dy));
                    a[dx][dy] = cnt;
                }
            }
        }
    }
}

int main(){
    
    cin >> N;

    for(int i = 0; i<N; i++){
        for(int j = 0; j<N; j++){
            scanf("%1d", &d[i][j]);}
    }

    int cnt = 0;

    for(int i = 0; i<N; i++){
        for(int j=0; j<N; j++){
            if(d[i][j] == 1 && a[i][j] == 0){
                bfs(i,j,++cnt);
            }
        }
    }    

    vector<int> v(cnt+1);

    for(int i = 0; i<=cnt;i++)
        v[i] = 0;
    
    for(int i = 0; i<N; i++){
        for(int j=0; j<N; j++){
            if(a[i][j] !=0)
                v[a[i][j]]++;
        }
    }
    printf("%d\n", cnt);
    sort(v.begin(), v.end());
    for(int i = 1; i<=cnt; i++)
        cout << v[i] << '\n';

    return 0;
}