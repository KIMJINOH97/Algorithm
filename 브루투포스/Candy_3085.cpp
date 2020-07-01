#include <iostream>
#include <cstdio>

using namespace std;
int N;
int nx[] = {1, 0};
int ny[] = {0, 1};
char a[51][51];
int swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
int m = -1;
void max_candy(){
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            for(int k=0; k<2; k++){
                int dx = i+ nx[k];
                int dy = j+ ny[k];
                int cnt=1;
                while(dx<N && dy<N){
                    if(a[i][j] == a[dx][dy]){
                        cnt++;
                        dx+=nx[k];
                        dy+=ny[k];
                    }
                    else
                        break;
                }
                if(cnt>m)
                    m = cnt;
            }
        }
    }
}
int main(){
    scanf("%d", &N);
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            scanf(" %1c", &a[i][j]);
        }
    }
    
    for(int i=0; i<N; i++){
        for(int j =0; j<N; j++){
            for(int k=0; k<2; k++){
                int dx = i+ nx[k];
                int dy = j+ ny[k];
                if(dx<N && dx>=0 && dy<N && dy>=0){
                    swap(a[i][j], a[dx][dy]);
                    max_candy();

                    swap(a[i][j], a[dx][dy]);
                }
            }
        }
    }
    cout << m << endl;
    return 0;
}