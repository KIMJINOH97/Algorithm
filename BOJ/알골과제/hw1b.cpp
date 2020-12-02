#include <iostream>
#include <algorithm>

using namespace std;

typedef struct bin{
    int left;
    int right;
    int level;
}bin;

bin tree[1001];
int cnt[1001];
int le[1001];

void init(){
    for(int i=0; i<1001; i++){
        tree[i].left = 0;
        tree[i].right = 0;
        tree[i].level = 1;
        cnt[i] =0;
        le[i] = 0;      
    }
}

void preorder(int k){
    if(k == -1)
        return ;
    preorder(tree[k].left);
    le[tree[k].level]++;
    preorder(tree[k].right);
}

int max_level(){
    int max = 0;
    for(int i=0; i<1001; i++){
        if(le[i] > max){
            max = le[i];
        }
    }
    for(int i=0; i<1001; i++){
        if(max == le[i])
            return i;
    }
}

int main(){

    int T, N;
    int a, b, c;
    int root;   
    cin >> T;
    while(T--){
        init();
        cin >> N;
        for(int i=0; i<N; i++){
            cin >> a >> b >> c;
            tree[a].left = b;
            tree[a].right = c;
            if(b != -1){
                cnt[b] += 1;
                tree[b].level = tree[a].level +1;
            }
            if(c != -1){
                cnt[c] += 1;
                tree[c].level = tree[a].level+1;
            }
        }
        for(int i=0; i<N; i++){
            if(cnt[i] == 0)
                root = i;
        }

        preorder(root);
        cout << max_level() << endl;
    }
    return 0;
}