#include <bits/stdc++.h>

using namespace std;

int main(){
    int N, K, L;
    cin >> N >> K; // 보드 크기 N, 사과 개수 K

    int arr[101][101];

    for(int i=0; i<K; i++){
        int dx, dy;
        cin >> dx >> dy;
        arr[dx-1][dy-1] = 1; // 사과가 있는 좌표 1
    }
    
    cin >> L; // 머리 회전 횟수
    vector<pair<int ,char>> round(L); // 머리 회전하는 시간, 및 방향 저장
    for(int i=0; i<L; i++){
        int a;
        char b;
        cin >> a >> b;
        round[i] = {a,b};
    }

    sort(round.begin(), round.end()); 

    int R = 0; // 현재 행좌표
    int C = 0; // 현재 열좌표
    int nr = 1; // 얼만큼 움직이는 행
    int nc = 0; // 얼만큼 움직이는 열
    int timer = 0; // 타이머
    int i = 0; // where의 인덱스
    int j = 0; // round의 인덱스
    arr[0][0] = 2; // 2로 표시된 건 뱀임
    vector<pair<int,int>> where(4);
    where = {{1,0}, {0,1}, {-1,0}, {0,-1}};
    deque<pair<int, int>> snake;
    snake.push_back({0,0}); // 첫 좌표 뱀
    
    while(1){ // 뱀 게임 시작
        if(j<L){
            if(round[j].first == timer){ // 현재 시간과 타이머의 일치
                if(round[j].second == 'D'){ // 오른쪽 90도 회전
                    i++;
                }
                if(round[j].second == 'L'){ // 왼쪽 90도 회전
                    i--;
                    if(i<0){
                        i+=4;
                    }
                }
                nr = where[abs(i%4)].first;
                nc = where[abs(i%4)].second;
                j++;
            }
        }
        // 직진
        R = R+nc;
        C = C+nr;
        timer++;

        int a = snake.front().first;
        int b = snake.front().second;
        if(R<0 || C<0 || R>=N || C>=N)
                break;
        if(arr[R][C] == 2)
            break;
        if(arr[R][C] == 0){ // 사과가 없을 때
            snake.pop_front();
            arr[a][b] = 0;
        }
        arr[R][C] = 2;
        snake.push_back({R,C});
    }
    

    printf("%d", timer);
    return 0;
}