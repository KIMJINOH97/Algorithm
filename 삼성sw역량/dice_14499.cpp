#include <bits/stdc++.h>

using namespace std;
int arr[20][20];
int nr[4] = {0, 0, -1, 1};
int nc[4] = {1, -1, 0, 0}; // 동서북남
int main(){
    int N,M,K,R,C; // N세로(행) M가로(열)
    cin >> N >> M >> R >> C >> K; // 세로, 가로, 주사위 좌표, 명령어개수
    vector<int> I(K);
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            int a;
            cin >> a;
            arr[i][j] = a;
        }
    }

    for(int i=0; i<K; i++){
        int b;
        cin >> b;
        I[i] = b;
    }

    for(int k=0; k<K; k++){
        int r = R+nr[I[k]-1]; // 현재 좌표 + 이동좌표
        int c = C+nc[I[k]-1];
        if(r < 0 || c < 0 || r >= N || c >= M ){ // 좌표 지도상 존재여부
            continue;
        }
        R = r; C = c; // 이동 한 좌표(R, C)
        if(I[k] == 1){ // 동

        }
        else if(I[k] == 2){ // 서

        }
        else if(I[k] == 3){ // 북

        }
        else{ // 남

        }
    }


    return 0;
}