#include <iostream>
#include <queue>
using namespace std;

int N;
char arr[101][101];
bool check[101][101];
bool check1[101][101];
int nx[] = {1, 0, -1, 0};
int ny[] = {0, 1, 0, -1};
queue<pair<int, int>> q;
void bfs(char c)
{
    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int k = 0; k < 4; k++)
        {
            int dx = x + nx[k];
            int dy = y + ny[k];
            if (dx < N && dx >= 0 && dy < N && dy >= 0)
            {
                if (check[dx][dy] == 0 && arr[dx][dy] == c)
                {
                    check[dx][dy] = 1;
                    q.push(make_pair(dx, dy));
                }
            }
        }
    }
}

void bfs(char a, char b)
{
    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int k = 0; k < 4; k++)
        {
            int dx = x + nx[k];
            int dy = y + ny[k];
            if (dx < N && dx >= 0 && dy < N && dy >= 0)
            {
                if (check1[dx][dy] == 0 && (arr[dx][dy] == a || arr[dx][dy] == b))
                {
                    check1[dx][dy] = 1;
                    q.push(make_pair(dx, dy));
                }
            }
        }
    }
    return;
}

int main()
{
    int c_red = 0;
    int c_blue = 0;
    int c_green = 0;
    int c_redgreen = 0;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
            cin >> arr[i][j];
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (check1[i][j] == 0 && (arr[i][j] == 'R' || arr[i][j] == 'G'))
            {
                check1[i][j] = 1;
                q.push(make_pair(i, j));
                bfs('R', 'G');
                c_redgreen++;
            }
            if (check[i][j] == 0 && arr[i][j] == 'R')
            {
                check[i][j] = 1;
                q.push(make_pair(i, j));
                bfs('R');
                c_red++;
            }
            if (check[i][j] == 0 && arr[i][j] == 'G')
            {
                check[i][j] = 1;
                q.push(make_pair(i, j));
                bfs('G');
                c_green++;
            }
            if (check[i][j] == 0 && arr[i][j] == 'B')
            {
                check[i][j] = 1;
                q.push(make_pair(i, j));
                bfs('B');
                c_blue++;
            }
        }
    }

    cout << c_red + c_blue + c_green << ' ' << c_redgreen + c_blue << endl;

    return 0;
}