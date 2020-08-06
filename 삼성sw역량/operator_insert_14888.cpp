#include <bits/stdc++.h>

using namespace std;
vector<char> oper;
vector<int> res;
int A[13];
bool check[13];
int N;

void dfs(int d, int s, char c){
    if(d == N-1){
        res.push_back(s);
        return ;
    }

    for(int i=0; i< N-1; i++){
        int su;
        if(check[d] != true){
            if(oper[d] == '+')
                su = s+A[i+1];
            else if(oper[d] == '-')
                su = s-A[i+1];
            else if(oper[d] == '*')
                su = s*A[i+1];
            else if(oper[d] == '/')
                su = s/A[i+1];
        }
        }
}

int main(){
    int op[4]; // {+,-,x,/}개수들 저장
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> A[i];
    }

    return 0;
}