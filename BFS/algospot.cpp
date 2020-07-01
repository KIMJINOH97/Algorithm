#include <iostream>
#include <cstdio>
#include <cstring>
#include <deque>
#include <tuple>

using namespace std;

int d[150][150];
int dist[150][150];
bool check[150][150];

int main(void)
{
    int N,M;
    deque<pair<int,int>> de;

    memset(d, -1, sizeof(d));
    cin >> M >> N;

    for(int i=0; i<N; i++)
    {
        for(int j=0; j<M; j++)
        {
            scanf("%1d", &d[i][j]);
        }
    }

    de.push_back(make_pair(0,0));
    check[0][0] = true;
    while(!de.empty())
    {
        int x,y;
        tie(x,y) = de.front();
        de.pop_front();

    if(x+1 < N)
    {
        if(d[x+1][y] != -1 && check[x+1][y] == false)
        {
            check[x+1][y] = true;
            if(d[x+1][y] == 0)
            {
                dist[x+1][y] = dist[x][y];
                de.push_front(make_pair(x+1,y));
            }
            else
            {
                dist[x+1][y] = dist[x][y] + 1;
                de.push_back(make_pair(x+1,y));
            }   
        }
    }
    if(y+1 < M)
    {
        if(d[x][y+1] != -1 && check[x][y+1] == false)
        {
            check[x][y+1] = true;
            if(d[x][y+1] == 0)
            {
                dist[x][y+1] = dist[x][y];
                de.push_front(make_pair(x,y+1));
            }
            else
            {
                dist[x][y+1] = dist[x][y] + 1;
                de.push_back(make_pair(x,y+1));
            }
        }
    }
    if(x-1 >= 0)
    {
        if(d[x-1][y] != -1 && check[x-1][y] == false)
        {
            check[x-1][y] = true;
            if(d[x-1][y] == 0)
            {
                dist[x-1][y] = dist[x][y];
                de.push_front(make_pair(x-1,y));
            }    
            else
            {
                dist[x-1][y] = dist[x][y] + 1;
                de.push_back(make_pair(x-1,y));
            }
        }
    }
    if(y-1 >= 0)
    {
        if(d[x][y-1] != -1 && check[x][y-1] == false)
        {
            check[x][y-1] = true;
            if(d[x][y-1] == 0)
            {
                dist[x][y-1] = dist[x][y];
                de.push_front(make_pair(x,y-1));
            }
            else
            {
                dist[x][y-1] = dist[x][y] + 1;
                de.push_back(make_pair(x,y-1));
            }  
        }
    }
    }

    printf("%d\n", dist[N-1][M-1]);

    return 0;
}