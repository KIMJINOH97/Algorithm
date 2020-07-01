#include <iostream>

using namespace std;

typedef struct Tree{
    char left;
    char right;
}Tree;

Tree T[101];

void init(){
    for(int i=0; i<101; i++){
        T[i].left = '0';
        T[i].right = '0';
    }
}

void preorder(char k){
    if(k == '0')
        return ;
    cout << k;
    preorder(T[k].left);
    preorder(T[k].right);
}

void inorder(char k){
    if(k=='0')
        return ;
    inorder(T[k].left);
    cout << k;
    inorder(T[k].right);
}

void postorder(char k){
    if(k=='0')
        return ;
    postorder(T[k].left);
    postorder(T[k].right);
    cout << k;
}

int main(void){

    init();
    int N;
    char a,b,c;
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> a >> b >> c;
        if(b != '.') T[a].left = b;
        if(c != '.') T[a].right = c;
    }

    preorder('A');
    cout << '\n';
    inorder('A');
    cout << '\n';
    postorder('A');
    return 0;
}