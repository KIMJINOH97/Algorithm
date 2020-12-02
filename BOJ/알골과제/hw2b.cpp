#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <time.h>

using namespace std;
vector<int> v1[6], v2[6];
float cl[20];
int A[10];
vector<int> sorted(100000000);
void merge(int low, int mid, int high, int n){
    int i = low;
    int j = mid+1;
    int k = low;
    while(i<=mid && j<= high){
        if(v1[n][i] <= v1[n][j]){
            sorted[k] = v1[n][i];
            i++;
        }
        else{
            sorted[k] = v1[n][j];
            j++;
        }
        k++;
    }
    if(i>mid){
        for(int t=j; t<=high; t++){
            sorted[k] = v1[n][t];
            k++;
        }
    }
    else{
        for(int t=i; t<=mid; t++){
            sorted[k] = v1[n][t];
            k++;
        }
    }
    for(int t = low; t<=high; t++){
        v1[n][t] = sorted[t];
    }
}

void msort(int low, int high, int n){
    int mid;
    if(low < high){
        mid = (low+high)/2;
        msort(low, mid, n);
        msort(mid+1, high, n);
        merge(low, mid, high, n);
    }
}

void pt(int low, int high, int &p_p, int n){
    int i,j, pi;
    pi = v2[n][low];
    j = low;
    for(i=low+1; i<=high; i++){
        if(v2[n][i] < pi){
            j++;
            int temp = v2[n][i];
            v2[n][i] = v2[n][j];
            v2[n][j] = temp;
        }
    }
        p_p = j;
        int temp = v2[n][low];
        v2[n][low] = v2[n][p_p];
        v2[n][p_p] = temp;
}
void qsort(int low, int high, int n){
    int pp;
    if(high > low){
        pt(low, high, pp, n);
        qsort(low, pp-1, n);
        qsort(pp+1, high, n);
    }
}

int main(){
    srand((unsigned int)time(NULL));
    int N;
    for(int i=0; i<6; i++){
        scanf("%d", &N); A[i] = N;
        for(int j=0; j<N; j++){
            int random = rand ();
            v1[i].push_back(random);
            v2[i].push_back(random);
        }
        if(i<3){ sort(v1[i].begin(), v1[i].end()); sort(v2[i].begin(), v2[i].end()); }
    }
    for(int i=0; i<6; i++){
        clock_t s = (int)clock();
        qsort(0, A[i]-1, i);
        cl[i] = (float)(clock() -s) / CLOCKS_PER_SEC;
        clock_t t = (int)clock();
        msort(0, A[i]-1, i);
        cl[i+6] = (float)(clock() -t) / CLOCKS_PER_SEC;
    }

    printf("--------------------sorted--------------------\n");
    printf("\t    N=%d \tN=%d      N=%d\n", A[0], A[1], A[2]);
    printf("----------------------------------------------\n");
    printf("Merge Sort  %.6lf      %.6lf      %.6lf\n", cl[6], cl[7], cl[8]);
    printf("Quick Sort  %.6lf      %.6lf      %.6lf\n\n\n", cl[0], cl[1], cl[2]); 


    printf("--------------------Random--------------------\n");
    printf("\t    N=%d\tN=%d     N=%d\n", A[3], A[4], A[5]);
    printf("----------------------------------------------\n");
    printf("Merge Sort  %.6lf      %.6lf      %.6lf\n", cl[9], cl[10], cl[11]);
    printf("Quick Sort  %.6lf      %.6lf      %.6lf\n", cl[3], cl[4], cl[5]); 

    return 0;
}
