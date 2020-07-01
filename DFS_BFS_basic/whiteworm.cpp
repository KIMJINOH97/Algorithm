#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

int M,N;
int a[51][51];
bool check[51][51];
int count;
int nx[] = {1, 0, -1, 0};
int ny[] = {0, -1, 0, 1};

void bfs(int s1, int s2){
    check[s1][s2] = true;
    queue<pair<int,int>> q;
    q.push(make_pair(s1,s2));
    while(!q.empty()){
        int x= q.front().first;
        int y= q.front().second;
        q.pop();

        for(int k = 0; k<4; k++){
            int dx = x + nx[k];
            int dy = y + ny[k];
            if(dx >=0 && dx <N && dy>=0 && dy<M){
                if(a[dx][dy] == 1 && check[dx][dy] == false){
                    check[dx][dy] = true;
                    q.push(make_pair(dx,dy));
                }
            }
        }
    }
    count++;
}

int main(){
    int T, K;

    cin >> T;
    while(T--){
        cin >> M >> N >> K;
        for(int i = 0; i<K; i++){
            int x, y;
            cin >> x >> y;
            a[y][x] = 1;
        }

        for(int i = 0; i<N; i++){
            for(int j = 0; j<M; j++){
                if(a[i][j] == 1 && check[i][j] == false){
                    bfs(i,j);
                }
            }
        }
        memset(check, false, sizeof(check));
        memset(a, 0, sizeof(a));
        cout << count << '\n';
        count = 0;
    }
    return 0;
}