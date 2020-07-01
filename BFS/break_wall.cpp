#include <cstdio>
#include <deque>

using namespace std;

int N,M;
int a[1001][1001];
int dist[1001][1001][2];
deque<pair<pair<int,int>,int>> d;
int nx[] = {1,0,-1,0};
int ny[] = {0,1,0,-1};

int bfs(){
    d.push_front(make_pair(make_pair(0,0),0));
    while(!d.empty()){
        int x = d.front().first.first;
        int y = d.front().first.second;
        int z = d.front().second;
        d.pop_front();

        if(x == N-1 && y == M-1 && dist[N-1][M-1][z] != 0)
            return dist[x][y][z];

        for(int k = 0; k<4; k++){
            int dx = x + nx[k];
            int dy = y + ny[k];

            if(dx<N && dx>=0 && dy<M && dy>=0){
                if(a[dx][dy]== 0 && dist[dx][dy][z] == 0){
                        d.push_back(make_pair(make_pair(dx,dy), z)); 
                        dist[dx][dy][z] = dist[x][y][z] + 1;
                }
                else if(a[dx][dy] == 1 && z == 0){
                    d.push_back(make_pair(make_pair(dx,dy),1));
                    dist[dx][dy][1] = dist[x][y][0] + 1;
                }
            }            
        }
    }
    return -1;
}

int main(){
    scanf("%d %d", &N, &M);

    for(int i = 0; i<N; i++){
        for(int j = 0; j<M; j++){
            scanf("%1d", &a[i][j]);
        }
    }
    dist[0][0][0] = 1;
    printf("%d", bfs());
    return 0;
}