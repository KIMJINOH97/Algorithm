#include <string>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers)
{
    vector<int> answer, real;
    for (int i = 0; i < numbers.size() - 1; i++)
    {
        for (int j = i + 1; j < numbers.size(); j++)
        {
            answer.push_back(numbers[i] + numbers[j]);
        }
    }
    sort(answer.begin(), answer.end());
    real.push_back(answer[0]);
    int last = 0;
    for (int i = 1; i < answer.size() - 1; i++)
    {
        if (answer[i] != real[last])
        {
            real.push_back(answer[i]);
            last++;
        }
    }
    int ans_last = answer.size() - 1;
    if (answer[ans_last] != answer[ans_last - 1])
        real.push_back(answer[ans_last]);
    return real;
}