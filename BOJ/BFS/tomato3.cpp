#include <iostream>
#include <deque>

using namespace std;
int M,N,H;
int a[101][101][101];
int nx[] = {1, 0, -1, 0, 0, 0};
int ny[] = {0, 1, 0, -1, 0, 0};
int nz[] = {0, 0, 0, 0, 1, -1};
deque<pair<pair<int,int>,int>> d;

void bfs(){
    for(int i = 0; i<H; i++){
        for(int j = 0; j<N; j++){
            for(int k=0; k<M; k++){
                if(a[j][k][i] == 1){
                    d.push_back(make_pair(make_pair(j,k), i));
                }
            }
        }
    }
    while(!d.empty()){
        int x = d.front().first.first;
        int y = d.front().first.second;
        int z = d.front().second;
        d.pop_front();

        for(int k = 0; k<6; k++){
            int dx = x + nx[k];
            int dy = y + ny[k];
            int dz = z + nz[k];

            if(dx< N && dx >=0 && dy<M && dy>=0 && dz<H && dz>=0){
                if(a[dx][dy][dz] == 0){
                    a[dx][dy][dz] = a[x][y][z] + 1;
                    d.push_back(make_pair(make_pair(dx,dy),dz));
                }
            }
        }
    }
}

int main(){

    cin >> M >> N >> H;
    for(int i = 0; i<H; i++){
        for(int j = 0; j<N; j++){
            for(int k=0; k<M; k++){
                cin >> a[j][k][i];
            }
        }
    }

    bfs();
    bool No = false;
    int count = -1;
    for(int i = 0; i<H; i++){
        for(int j = 0; j<N; j++){
            for(int k=0; k<M; k++){
                if(a[j][k][i] == 0){
                    No = true;
                }
                if(a[j][k][i] > count){
                    count = a[j][k][i];
                }
            }
        }
    }

    if(No == true){
        cout << "-1" << endl;
    }
    else
    {
        cout << count-1 << endl;
    }
    
    return 0;
}