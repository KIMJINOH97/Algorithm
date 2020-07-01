#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

bool check[301][301];
int d[301][301];

int nx[] = {2, 1, -1, -2, -2, -1, 1, 2};
int ny[] = {1, 2, 2, 1, -1, -2, -2, -1};

int main(){

    int T,x,a,b,A,B;
    cin >> T;

    while(T--)
    {
        memset(check, false, sizeof(check));
        memset(d, 0, sizeof(d));
        
        cin >> x >> a >> b >> A >> B;
        
        check[a][b] = true;

        queue<pair<int ,int>> q;
        q.push(make_pair(a, b));

        while(!q.empty()){
            int x1 = q.front().first;
            int y1 = q.front().second;
            q.pop();

            for(int k = 0; k<8; k++){
                int dx = x1 + nx[k];
                int dy = y1 + ny[k];

                if(dx < x && dx >=0 && dy < x && dy >=0){
                    if(check[dx][dy] == false){
                        d[dx][dy] = d[x1][y1] + 1;
                        check[dx][dy] = true;
                        q.push(make_pair(dx,dy));
                    }
                }
            }
            if(check[A][B] == true)
                break;
        }

        cout << d[A][B] << '\n';
    }

    return 0;
}