#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <tuple>
#define MAX 1000

using namespace std;

int d[MAX+1][MAX+1];

int main(void)
{
    int n;
    cin >> n;
    memset(d, -1, sizeof(d));

    queue<pair<int, int>> q;
    q.push(make_pair(1,0));
    d[1][0] = 0;
    while(!q.empty())
    {
        int s,c;
        tie(s,c) = q.front();
        q.pop();
        if(s<=n && d[s][s] == -1)
        {
            d[s][s] = d[s][c] + 1;
            q.push(make_pair(s,s));
        }
        if(s+c <= n && d[s+c][c] == -1)
        {
            d[s+c][c] = d[s][c] + 1;
            q.push(make_pair(s+c,c));
        }
        if(s-1 >=0 && d[s-1][c] == -1)
        {
            d[s-1][c] = d[s][c] + 1;
            q.push(make_pair(s-1,c));
        }
    }

int ans = MAX;
for(int i = 0; i<n; i++)
{
   if(d[n][i] > 0 && ans > d[n][i])
    ans = d[n][i];
}

cout << ans << endl;
    return 0;
}