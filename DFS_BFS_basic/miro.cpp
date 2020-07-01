#include <cstdio>
#include <queue>

using namespace std;

int a[101][101];
int d[101][101];
int nx[] = {1,0,-1,0};
int ny[] = {0,1,0,-1};

int main(void){
    int N,M;

    scanf("%d %d", &N, &M);

    for(int i = 0; i<N; i++){
        for(int j = 0; j<M; j++){
            scanf("%1d", &a[i][j]);
        }
    }

    queue<pair<int,int>> q;
    
    q.push(make_pair(0,0));
    d[0][0] = 1;

    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for(int k=0; k<4; k++){
            int dx = x+nx[k];
            int dy = y+ny[k];

            if(dx >=0 && dx < N && dy >=0 && dy <M){
                if(a[dx][dy] == 1 && d[dx][dy] == 0){
                    q.push(make_pair(dx,dy));
                    d[dx][dy] = d[x][y] + 1;
                }
            }
        }
    }

    printf("%d\n", d[N-1][M-1]);
    
    return 0;
}