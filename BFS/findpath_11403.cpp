#include <iostream>
#include <queue>
using namespace std;

int N;
int arr[101][101];
int ans[101][101];
queue<pair<int, int>> q;

void bfs()
{
    int x = q.front().first;
    while (!q.empty())
    {
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < N; i++)
        {
            if (arr[y][i] == 1 && ans[x][i] == 0)
            {
                ans[x][i] = 1;
                q.push(make_pair(y, i));
            }
        }
    }
    return;
}

int main()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> arr[i][j];
        }
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (arr[i][j] == 1)
            {
                ans[i][j] = 1;
                q.push(make_pair(i, j));
                bfs();
            }
        }
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout << ans[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}