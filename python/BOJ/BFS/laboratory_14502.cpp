#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;
int N, M; // 세로 가로 크기
int arr[9][9];
int a[9][9];              // 임시배열
int dx[] = {1, 0, -1, 0}; // 시계방향
int dy[] = {0, 1, 0, -1};
int max_b = 0;
int tmp[9][9];
void bfs()
{
    queue<pair<int, int>> q;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            tmp[i][j] = a[i][j];
            if (a[i][j] == 2)
                q.push(make_pair(i, j));
        }
    }

    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int k = 0; k < 4; k++)
        {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < N && nx >= 0 && ny < M && ny >= 0)
            {
                if (tmp[nx][ny] == 0)
                {
                    tmp[nx][ny] = 2;
                    q.push(make_pair(nx, ny));
                }
            }
        }
    }

    int count = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (tmp[i][j] == 0)
                count++;
        }
    }
    max_b = max(max_b, count);
    return;
}

void init()
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            a[i][j] = arr[i][j];
        }
    }
}

void wall(int cnt)
{
    if (cnt == 3)
    {
        bfs();
        return;
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (a[i][j] == 0)
            {
                a[i][j] = 1;
                wall(cnt + 1);
                a[i][j] = 0;
            }
        }
    }
    return;
}

int main()
{
    cin >> N >> M;
    int zero_count = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> arr[i][j];
            if (arr[i][j] == 0)
            {
                zero_count++;
            }
        }
    }

    init();
    wall(0);
    cout << max_b << endl;
    return 0;
}