#include <iostream>
#define max 105
using namespace std;

int N;
float P[max];
float A[max][max];
int R[max][max];

typedef struct Node{
    int key;
    int left;
    int right;
}node;

node obst[max];
void init_obst(){
    for(int i=0; i<max; i++){
        obst[i].key = i;
        obst[i].left = 0;
        obst[i].right = 0;
    }
}

void init(){
    for(int i=0; i<max; i++){
        for(int j=0; j<max; j++){
            A[i][j] = 0;
            R[i][j] = 0;
        }
        P[i] = 0;
    }
}

void opt(int n){
    int i,j,k,d;
    for(int i=1; i<=n; i++){
        A[i][i] = P[i];
        R[i][i] = i;
    }
    for(d=1; d<=n-1; d++){
        for(i=1; i<=n-d; i++){
            j = d+i;
            float p_s=0;
            for(k=i; k<=j; k++){
                p_s += P[k];
            }
            float min=99999999;
            int val_k;
            for(k=i; k<=j; k++){
                int o = A[i][k-1] + A[k+1][j];
                if(o < min){
                    min = o;
                    val_k = k;
                }
            }
            A[i][j] = min+p_s;
            R[i][j] = val_k;
        }
    }
    /*for(i=1; i<=n; i++){
        for(j=1; j<=n; j++){
            cout << R[i][j] << " ";
        }
        cout << endl;
    }*/
}

int tree(int i, int j){
    int k;
    k=R[i][j];
    if(k==0)
        return -1;
    else{
        obst[k].left = tree(i,k-1);
        obst[k].right = tree(k+1,j);
        return k;
    }
}

void preorder(int k){
    if(k == -1)
        return ;
    cout << obst[k].key << " ";
    preorder(obst[k].left);
    preorder(obst[k].right);
}

int main(){
    int T;
    cout << "Test Case : ";
    cin >> T;
    while(T--){
        init();
        init_obst();
        cout << "number of number : ";
        cin >> N;
        for(int i=1; i<=N; i++)
            cin >> P[i];
        opt(N);
        tree(1,N);
        preorder(R[1][N]);
        cout << endl;
    }

    return 0;
}