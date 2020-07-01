#include <iostream>
#include <queue>

using namespace std;

int d[1001][1001];
int s[1001][1001];
bool check[1001][1001];

int nx[] = {1, 0, -1, 0};
int ny[] = {0, +1, 0, -1};

int main(){
    int M, N;

    cin >> M >> N;

    queue<pair<int,int>> q;

    for(int i = 0; i<N; i++){
        for(int j=0; j<M; j++){
            cin >> s[i][j];
            if(s[i][j] != 0){
                if(s[i][j] == 1){
                    q.push(make_pair(i,j));
                }
                check[i][j] = true;
            }
        }
    }

    int out = 0;

    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        for(int k = 0; k<4; k++){
            int dx = x + nx[k];
            int dy = y + ny[k];

            if(dx >= 0 && dx < N && dy >= 0 && dy < M){
                if(s[dx][dy] == 0){
                    check[dx][dy] = true;
                    q.push(make_pair(dx,dy));
                    s[dx][dy] = s[x][y] + 1;
                }
            }
        }        
    }

    int second = 0;

for(int i = 0; i<N; i++){
            for(int j =0; j<M; j++){
                if(check[i][j] == false)
                    out = 1;
            }
        }

    if(out == 1)
        cout << "-1" << '\n';
    else{
        for(int i = 0; i<N; i++){
            for(int j=0; j<M; j++){
                if(s[i][j] > second){
                    second = s[i][j];
                }
            }
        }
        cout << second-1 << '\n';
        
    }

    return 0;
}