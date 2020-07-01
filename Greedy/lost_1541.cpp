#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace std;
//48~57
vector<int> n;
vector<char> sym;

void greedy(){
    int sum = 0;
    int result = n[0];
    bool minus = false;
    int j=1;
    for(int i=0; i<sym.size()-1; i++){
        if(sym[i] == '+'){
            if(minus == true){
                sum += n[j];
            }
            else{
                result += n[j];
            }
        }
        else{
            minus = true;
            sum += n[j];
        }
        j++;
    }
    result -= sum;
    cout << result << endl;
}

int main(){
    string s;
    cin >> s;
    stack<int> change;
    int mul = 1;
    int c = 0;
    for(int i=0; i<=s.length(); i++){
        if(s[i] == '+' || s[i] == '-' || i == s.length()){
            while(!change.empty()){
                c += (change.top() * mul);
                change.pop();
                mul *= 10;
            }
            n.push_back(c);
            mul = 1;
            c= 0;  
            sym.push_back(s[i]);
        }
        else{
            change.push(s[i] - 48);
        }
    }

    greedy();

    return 0;
}