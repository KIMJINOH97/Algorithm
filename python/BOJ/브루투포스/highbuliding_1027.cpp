#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int N;
    double arr[50];
    int c[50];
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    for (int i = 0; i < N; i++)
    {
        int count = 0;
        for (int j = i + 1; j < N; j++)
        {
            double incline = (arr[j] - arr[i]) / (j - i); // 기울기
            bool check = true;
            for (int k = i + 1; k < j; k++)
            {
                double tmp = (arr[k] - arr[i]) / (k - i); // 비교할 기울기
                if (tmp >= incline)
                {
                    check = false;
                    break;
                }
            }
            if (check == true)
            {
                count++;
            }
        }
        for (int j = 0; j < i; j++)
        {
            double incline = (arr[j] - arr[i]) / (j - i); // 기울기
            bool check = true;
            for (int k = j + 1; k < i; k++)
            {
                double tmp = (arr[k] - arr[i]) / (k - i); // 비교할 기울기
                if (tmp <= incline)
                {
                    check = false;
                    break;
                }
            }
            if (check == true)
            {
                count++;
            }
        }
        c[i] = count;
    }

    int m = 0;
    for (int i = 0; i < N; i++)
    {
        if (m < c[i])
        {
            m = c[i];
        }
    }

    cout << m << endl;

    return 0;
}