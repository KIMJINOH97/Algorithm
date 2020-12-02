#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#define MAX 100001

using namespace std;

bool check[MAX];
int dist[MAX];

queue<int> q;


void bfs(int x, int y)
{
	check[x] = true;
	q.push(x);
	while (!q.empty())
	{
		int now = q.front();
		q.pop();
		if (now - 1 >= 0 && check[now - 1] == false)
		{
			q.push(now - 1);
			check[now - 1] = true;
			dist[now - 1] = dist[now] + 1;
		}

		if (now + 1 < MAX && check[now+1] == false)
		{
			q.push(now + 1);
			check[now + 1] = true;
			dist[now + 1] = dist[now] + 1;
		}

		if (2 * now < MAX && check[2*now] == false)
		{
			q.push(now * 2);
			check[now * 2] = true;
			dist[now * 2] = dist[now] + 1;
		}
	}
	cout << dist[y] << endl;
}

int main(void)
{
	int N, K;

	cin >> N >> K;
	bfs(N, K);

	return 0;
}