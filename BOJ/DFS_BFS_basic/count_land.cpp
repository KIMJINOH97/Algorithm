#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

int s[51][51];
bool check[51][51];

int nx[] = {0,0,1,1,1,-1,-1,-1};
int ny[] = {1,-1,0,1,-1,0,1,-1};
int w,h;

void bfs(int x, int y, int cnt)
{
    queue<pair<int, int>> q;
    q.push(make_pair(x,y));
    check[x][y] = true;
    while(!q.empty()){
        x = q.front().first;
        y = q.front().second;
        q.pop();

        for(int i = 0; i<8; i++){
            int dx = x+nx[i];
            int dy = y+ny[i];
            if(dx >= 0 && dx <h && dy >=0 && dy < w){
                if(check[dx][dy] == false && s[dx][dy] ==1){
                    check[dx][dy] = true;
                    q.push(make_pair(dx,dy));
                }
            }
        }
    }
}

int main(){

    while(1){
        cin >> w >> h;
        if(w == 0 && h == 0)
            break;
        
        for(int i=0; i<h; i++){
            for(int j=0; j<w; j++){
                cin >> s[i][j];
            }
        }

        int cnt = 0;

        for(int i=0; i<h; i++){
            for(int j=0; j<w; j++){
                if(check[i][j] == false && s[i][j] == 1){
                    bfs(i,j,++cnt);
                }
            }
        }

        cout << cnt << '\n';
        memset(check, false, sizeof(check));
    }

    return 0;
}