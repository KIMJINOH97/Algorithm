#include <iostream>

using namespace std;

int main()
{
    int N;
    cin >> N;
    int arr[11];
    int line[11];
    for (int i = 1; i <= N; i++)
    {
        cin >> arr[i];
        line[i] = 0;
    }

    for (int i = 1; i <= N; i++)
    {
        int count = 0;
        for (int j = 1; j <= N; j++)
        {
            if (arr[i] == count && line[j] == 0)
            {
                line[j] = i;
                break;
            }
            if (line[j] == 0)
            {
                count++;
            }
        }
    }

    for (int i = 1; i <= N; i++)
    {
        cout << line[i] << ' ';
    }
    return 0;
}