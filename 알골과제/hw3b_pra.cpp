#include <iostream>

using namespace std;

typedef struct Node{
    int key;
    int left;
    int right;
}node;

node bst[101];
double P[101];
double A[6][6];
int R[6][6];

int main(){
    int T;
    /*cin >> T;
    for(int i=0; i<T; i++){
        int N;
        cin >> N;
        for(int j=0; j<N; j++){

        }
         
    }*/
    int n=4;
    P[1] = 0.375;
    P[2] = 0.375;
    P[3] = 0.125;
    P[4] = 0.125;

    for(int i=1; i<=n; i++){
        R[i][i] = i;
        A[i][i] = P[i];
    }
    A[n+1][n] = 0;
    R[n+1][n] = 0;
    int i,j,k;
    for(int d=1; d<=n-1; d++){
        for(i=1; i<=n-d; i++){
            j= i+d;
            double s=0;
            double min=999999;
            int val_k;
            for(k=i; k<=j; k++){
                if(A[i][k-1]+A[k+1][j] <min){
                    min = A[i][k-1]+A[k+1][j];
                    val_k = k;
                }
                s += P[k];
            }    
            A[i][j] = min+s;
            R[i][j] = val_k;
        }
    }
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n; j++){
            printf("%lf", A[i][j]);
        }
        cout << endl;
    }
    return 0;
}