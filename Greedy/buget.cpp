#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;
int solution(vector<int> budgets, int M)
{
    int sum = 0;

    if (budgets[0] >= M)
    {
        return (M / budgets.size());
    }

    for (int i = 0; i < budgets.size(); i++)
    {
        sum += budgets[i];
    }

    if (sum <= M)
    {
        return budgets.back();
    }
    else
    {
        int check = 0;
        int s = 0;
        for (int i = 0; i < budgets.size(); i++)
        {
            s += budgets[i];
            check = s + budgets[i] * (budgets.size() - i - 1);
            if (check > M)
            {
                int tmp = budgets[i - 1];
                int ch = s - budgets[i];
                int ans = (M - ch) / (budgets.size() - i);
                return ans;
            }
        }
    }
    return 1;
}

int main()
{
    int N; // 지방 수
    int M;
    cin >> N;
    vector<int> budgets(N);
    for (int i = 0; i < N; i++)
    {
        cin >> budgets[i];
    }
    cin >> M;
    sort(budgets.begin(), budgets.end());
    cout << solution(budgets, M) << endl;

    return 0;
}