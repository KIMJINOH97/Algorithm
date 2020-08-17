#include <bits/stdc++.h>

using namespace std;

int nr[] = {0, 1, 0, -1};
int nc[] = {1, 0, -1, 0};
int N, L, R;  // N*N 행렬
int A[51][51], check[51][51];
int country = 1;    // 각 연합국 마다 번호 매겨줌
bool flag = false;  // 연합국 존재? 위한 플래그
queue<pair<int, int>> q;
vector<pair<int, int>> v;  // 나라, 개수, 연합 총 인구
int count_country;
int count_people;
void bfs() {
    while (!q.empty()) {
        int r = q.front().first;
        int c = q.front().second;
        q.pop();
        for (int k = 0; k < 4; k++) {
            int dr = r + nr[k];
            int dc = c + nc[k];
            int dif = abs(A[dr][dc] - A[r][c]);
            if (dr >= 0 && dr < N && dc >= 0 && dc < N) {
                if (dif >= L && dif <= R && check[dr][dc] == 0) {
                    check[r][c] = country;
                    check[dr][dc] = country;
                    flag = true;  // 연합국 존재
                    count_country++;
                    count_people += A[dr][dc];
                    q.push({dr, dc});
                }
            }
        }
    }
}

void bfs_move(int c_num) {
    while (!q.empty()) {
        int r = q.front().first;
        int c = q.front().second;
        q.pop();
        for (int k = 0; k < 4; k++) {
            int dr = r + nr[k];
            int dc = c + nc[k];
            if (dr >= 0 && dr < N && dc >= 0 && dc < N) {
                if (check[dr][dc] == c_num) {
                    check[dr][dc] = 0;
                    A[dr][dc] = v[c_num - 1].second / v[c_num - 1].first;
                    q.push({dr, dc});
                }
            }
        }
    }
}

int main() {
    cin >> N >> L >> R;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> A[i][j];
        }
    }

    int count_move = 0;
    while (1) {
        country = 1;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (check[i][j] == 0) {
                    q.push({i, j});
                    count_country = 1;
                    count_people = A[i][j];
                    bfs();
                    if (flag) {
                        v.push_back({count_country, count_people});
                        country++;  // 연합국이 존재 함.
                        flag = false;
                    }
                }
            }
        }
        if (country == 1)
            break;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (check[i][j] != 0) {
                    q.push({i, j});
                    bfs_move(check[i][j]);
                }
            }
        }
        count_move++;
        v.clear();
    }
    cout << count_move << endl;
    return 0;
}