#include <bits/stdc++.h>

using namespace std;
vector<pair<int, int>> v(4);

void route_left(){
    int a = v[3].first;
    int b = v[3].second;
    v[3] = v[2];
    v[2] = v[1];
    v[1] = v[0];
    v[0].first = a;
    v[0].second = b;
}

int main(){
    int N,M, r, c, d;
    int arr[51][51];
    cin >> N >> M >> r >> c >> d;

    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            cin >> arr[i][j];
        }
    }
    // 0,1,2,3 북 동 남 서 d = 0 즉 북쪽을 가리킬 때
    v = {{-1,0}, {0,1}, {1,0}, {0,-1}};
    int cnt = 1; // 청소한 칸 수 세기 맨 처음 청소 = 1
    arr[r][c] = 2;
    int route = 0; // 네 방향 모두 청소?
    for(int i=0; i<4-d; i++){
        route_left();
    }

    while(1){
        d--; // 좌회전
        if(d<0)
            d+=4;
        route_left();
        route++; // 회전 한 번 할 때 마다 더해주기
        int R = r+v[0].first;
        int C = c+v[0].second;
        if(R<0 || C<0 || R>= N || C>=M){ // 범위를 벗어 났을 때
            continue;
        }
        if(arr[R][C] == 0){ // 청소가 안된 칸일 경우
            r = R; c = C; route = 0; // 전진한다.
            arr[r][c] = 2; cnt++; // 청소한 후 횟수증가
        }else{ // 청소 돼있거나 벽 일 경우
            if(route == 4){ // 네 방향 전부 청소거나 벽일 경우
                R = r+v[2].first; // 후진
                C = c+v[2].second;
                if(arr[R][C] == 1 || R<0 || C<0 || R>=N || C>=M) // 벽이거나 바깥이면 게임 끝
                    break;
                r = R; c = C; route =0; // 후진 이동 시키고 회전 횟수 0
            }
        }
    //      cout << endl;
    //      for(int i=0; i<N; i++){
    //      for(int j=0; j<M; j++){
    //          cout << arr[i][j] << ' ';
    //      }
    //      cout << endl;
    //  }
    }
    cout << cnt << endl;
    return 0;
}