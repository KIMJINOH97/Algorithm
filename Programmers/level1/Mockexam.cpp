#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int count[3] = {0,};
    int firstStudent[5] = {1,2,3,4,5};
    int secondStudent[8] = {2,1,2,3,2,4,2,5};
    int thirdStudent[10] = {3,3,1,1,2,2,4,4,5,5};
    
    int maxAnswer = -1;
    
    for(int i=0; i<answers.size(); i++){
        if(firstStudent[i%5] == answers[i]) count[0]++;
        if(secondStudent[i%8] == answers[i]) count[1]++;
        if(thirdStudent[i%10] == answers[i]) count[2]++;
    }
    
    for(int j=0; j<3; j++){
        if(count[j] > maxAnswer){
            maxAnswer = count[j];
        }
    }
    
    for(int j=0; j<3; j++){
        if(maxAnswer == count[j]){
            answer.push_back(j+1);
        }
    }
    
    return answer;
}