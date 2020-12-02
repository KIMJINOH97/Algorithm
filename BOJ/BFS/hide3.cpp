#include <iostream>
#include <deque>
#define MAX 100000
using namespace std;

int dist[MAX+1];
bool check[MAX+1];

int main(void)
{
    int N, K;
    cin >> N >> K;

    deque<int> d;
    check[N] = true;
    d.push_back(N);
    
    while(!d.empty())
    {
        int now = d.front();
        d.pop_front();
        if(2*now <= MAX && check[2*now] == false)
        {
            d.push_front(2*now);
            dist[2*now] = dist[now];
            check[2*now] = true;
        }
        if(now+1 <= MAX && check[now+1] == false)
        {
            d.push_back(now+1);
            dist[now+1] = dist[now] + 1;
            check[now+1] = true;
        }
        if(now-1 >= 0 && check[now-1] == false)
        {
            d.push_back(now-1);
            dist[now-1] = dist[now] + 1;
            check[now-1] = true;
        }
    }

    cout << dist[K] << '\n';

    return 0;
}