#include <iostream>

using namespace std;

int arr[10];

int pt(int low, int high){
    int pivot = arr[low];
    int i, j;
    i = low+1;
    j = low;
    for(; i<=high; i++){
        if(arr[i]<=pivot){
            j++;
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
    }
    int tmp = arr[j];
    arr[j] = pivot;
    arr[low] = tmp;
    return j;
}

void q_sort(int low, int high){
    if(low < high){
        int p = pt(low, high);
        q_sort(low, p-1);
        q_sort(p+1, high);
    }
}

int main(){
    for(int i=0; i<10; i++)
        cin >> arr[i];
    q_sort(0,9);

    for(int i=0; i<10; i++)
        cout << arr[i] << ' ';
    return 0;
}