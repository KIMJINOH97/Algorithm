#include <iostream>
#include <queue>
#include <vector>
#include <stack>
#define MAX 100001

using namespace std;

int from[MAX];
int dist[MAX];
bool check[MAX];
queue<int> q;
stack<int> s;

void bfs(int x, int y)
{
    check[x] = true;
    q.push(x);
    while(!q.empty())
    {
        int now = q.front();
        q.pop();
        if(now+1 < MAX && check[now+1] == false)
        {
            q.push(now+1);
            from[now+1] = now;
            dist[now+1] = dist[now] + 1;
            check[now+1] = true; 
        }

        if(now-1 >= 0 && check[now-1] ==false)
        {
            q.push(now-1);
            from[now-1] = now;
            dist[now-1] = dist[now] +1;
            check[now-1] = true;
        }

        if(now *2 < MAX && check[2*now] == false)
        {
            q.push(now*2);
            from[now*2] = now;
            dist[2*now] = dist[now] + 1;
            check[2*now] = true;
        }
    }
    cout << dist[y] << endl;
    for(int i = y; i != x; i=from[i])
    {
        s.push(from[i]);
    }
    while(!s.empty())
    {
        cout << s.top() << " ";
        s.pop();
    }

    cout << y;
}

int main()
{
    int N,M;
    cin >> N >> M;
    bfs(N,M);
    return 0;
}