#include <iostream>

using namespace std;
int arr[10];
int sorted[10];
void merge(int low, int mid, int high){
    int i,j,k;
    i=low;
    j=mid+1;
    k=low;
    while(i<=mid && j<=high){
        if(arr[i] <= arr[j]){
            sorted[k] = arr[i];
            i++;
        }
        else{
            sorted[k] = arr[j];
            j++;
        }
        k++;
    }
    if(i<=mid){
        for(int t=i; t<=mid; t++){
            sorted[k] = arr[t];
            k++;
        }
    }
    else{
        for(int t=j; t<=high; t++){
            sorted[k] = arr[t];
            k++;
        }
    }
    for(int t=low; t<=high; t++)
        arr[t] = sorted[t];
}

void m_sort(int low, int high){
    if(low<high){
        int mid = (low+high)/2;
        m_sort(low, mid);
        m_sort(mid+1, high);
        merge(low, mid, high);
    }
}

int main(){

    for(int i=0; i<10; i++)
        cin >> arr[i];
    m_sort(0, 9);
    for(int i=0; i<10; i++)
        cout << arr[i] << ' ';

    return 0;
}