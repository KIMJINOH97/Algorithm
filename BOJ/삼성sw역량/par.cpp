#include <iostream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;

string copy_s(string s1, int first, int last){
    string c_s;
    for(int i=first; i<=last; i++){
        c_s.push_back(s1[i]);
    }
    return c_s;
}

int main(){
    int answer = 0; string s = "ababcdcdababcdcd";
    int len = s.size(); int max_div = len/2;
    string compress_s;
    vector<int> v;
    v.push_back(len);
    
    for(int i=1; i<=max_div; i++){
        // i는 자르는 개수
        int count = 1; // 중복된 문자열 수
        string c_s=copy_s(s,0, i-1);
        int last_index = len-1;
        int j = i;
        while(1){
            if(j+i-1 >= last_index){
                // 비교할 문자열이 len 이상일 때
                string last = copy_s(s, j, last_index);
                if(j+i-1 == last_index && last == c_s){
                    count++;
                }
                if(count>1){
                    string repeat=to_string(count);
                    compress_s += repeat;
                }
                compress_s+=c_s;
                if(j+i-1 == last_index && last != c_s){
                    compress_s += last;
                }
                if(j+i-1 != last_index){
                    compress_s += last;
                }
                v.push_back(compress_s.size());
                compress_s.clear();
                break;
            }
            string next_cs = copy_s(s,j,j+i-1);
            if(c_s == next_cs){
                count++;
            }
            else{
                    // 비교하는 문자열과 같지 않을 때
                if(count >1){
                    string repeat=to_string(count);
                    compress_s += repeat;
                }
                compress_s += c_s;
                c_s=next_cs;
                count=1;
            }
            j+=i;
        }
    }
    sort(v.begin(), v.end());
    cout << v[0] << endl;
    return 0;
}
