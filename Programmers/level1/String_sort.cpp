#include <string>
#include <algorithm>
#include <vector>

using namespace std;
int index;
bool compare(string i, string j)
{
    if (i[index] == j[index])
        return i < j;
    return i[index] < j[index];
}

vector<string> solution(vector<string> strings, int n)
{
    vector<string> answer;
    index = n;
    sort(strings.begin(), strings.end(), compare);

    return strings;
}