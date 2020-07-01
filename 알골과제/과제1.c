#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Tree{
    int Number;
    struct Tree *left;
    struct Tree *right;
}Tree;

Tree bin[1001];
int T,N;
int high[1001];
int max;
Tree *root = NULL;
Tree *s = NULL;

void init(){
    for(int i=0; i<1001; i++){
        bin[i].left = NULL;
        bin[i].right = NULL;
    }
}

struct Tree* search(struct Tree* r, int find){
    if(r->Number == find)
        return r;
    if(r != NULL){
        search(r->left, find);
        search(r->right,find);
    }
}

int height(struct Tree *r, int h){
    if(r==NULL)
        return 0;
    else{
        int left_h = height(r->left, h);
        int right_h = height(r->right,h);
        return 1+(left_h > right_h ? left_h : right_h);
    }
}

int max_height(){
    for(int i=0; i<1001; i++){
        if(high[i] > max){
            max = high[i];
        }
    }
    for(int j=0; j<1001; j++){
        if(max == high[j])
            return j;
    }
}

int main(){

    init();
    scanf("%d", &T);
    int n=0;
    while(T--){
        scanf("%d", &N); // 데이터 노드 수
        for(int i=0; i<N; i++){
            int node, l, r;
            scanf("%d %d %d", &node, &l, &r);
            
            bin[n].Number = node;
            if(l == -1){
                bin[n].left = NULL;
            }
            else if(r == -1){
                bin[n].right = NULL;
            }
            else{
                *bin[n].left = bin[++n];
                *bin[n].right = bin[++n];
            }
        }
        printf("%d\n", max_height());
        memset(high, 0, sizeof(high));
        root = NULL;
    }

    return 0;
}