#include <string>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands)
{
    vector<int> answer, temp;

    for (int i = 0; i < commands.size(); i++)
    {
        int firstIndex = commands[i][0] - 1;
        int lastIndex = commands[i][1] - 1;
        int Index = commands[i][2] - 1;

        for (int j = firstIndex; j <= lastIndex; j++)
        {
            temp.push_back(array[j]);
        }
        sort(temp.begin(), temp.end());
        answer.push_back(temp[Index]);
        temp.clear();
    }
    return answer;
}