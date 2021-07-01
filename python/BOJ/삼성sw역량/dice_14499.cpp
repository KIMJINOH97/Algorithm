#include <bits/stdc++.h>

using namespace std;
int arr[21][21];
int nr[4] = {0, 0, -1, 1};
int nc[4] = {1, -1, 0, 0}; // 동서북남
int dice[6] = {0, 0, 0, 0, 0, 0}; // 위 아래 앞 뒤 왼 오

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

    if(arr[R][C] == 0){
            arr[R][C] = dice[1]; // 주사위 바닥 값을 지도 칸에 복사
    }
    else{
        dice[1] = arr[R][C]; // 주사위 바닥값에 지도 칸의 값을 복사
        arr[R][C] = 0;
    }


    for(int k=0; k<K; k++){
        int r = R+nr[I[k]-1]; // 현재 좌표 + 이동좌표
        int c = C+nc[I[k]-1];
        if(r < 0 || c < 0 || r >= N || c >= M ){ // 좌표 지도상 존재여부
            continue;
        }
        R = r; C = c; // 이동 한 좌표(R, C)
        
        int temp[6] = {0,};
        for(int j =0; j<6; j++){
            temp[j] = dice[j];
        }

        if(I[k] == 1){ // 동
            dice[0] = temp[5];
            dice[1] = temp[4];
            dice[4] = temp[0];
            dice[5] = temp[1];
        }
        else if(I[k] == 2){ // 서
            dice[0] = temp[4]; // 윗면이 과거 좌측
            dice[1] = temp[5]; // 아랫면이 과거 우측
            dice[4] = temp[1];
            dice[5] = temp[0];
        }
        else if(I[k] == 3){ // 북
            dice[0] = temp[2];
            dice[1] = temp[3];
            dice[2] = temp[1];
            dice[3] = temp[0];
        }
        else{ // 남
            dice[0] = temp[3];
            dice[1] = temp[2];
            dice[2] = temp[0];
            dice[3] = temp[1];
        }   

        if(arr[R][C] == 0){
            arr[R][C] = dice[1]; // 주사위 바닥 값을 지도 칸에 복사
        }
        else{
            dice[1] = arr[R][C]; // 주사위 바닥값에 지도 칸의 값을 복사
            arr[R][C] = 0;
        }

        cout << dice[0] << '\n';
    }
    
    return 0;
}