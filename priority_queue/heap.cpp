#include <iostream>
#define N 100001
using namespace std;
int heap_count = 0;
int heap[N];
int arr[N];

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void push(int data){
    heap[++heap_count] = data;
    int child = heap_count;
    int parent = child / 2;
    while(child > 1 && heap[parent] < heap[child]){
        swap(&heap[parent], &heap[child]);
        child = parent;
        parent = child/ 2;
    }
}

int pop(){
    int p = heap[1];

    swap(&heap[1], &heap[heap_count]);
    heap_count--;

    int parent = 1;
    int child = 2;

    if(heap_count >= child+1){
        child = (heap[child]> heap[child+1])? child:child+1;
    }

    while(child<=heap_count && heap[parent] < heap[child]){
        swap(&heap[parent], &heap[child]);
        parent = child;
        child = child*2;
        if(child+1 <= heap_count){
            child = (heap[child] > heap[child+1])? child:child+1;
        }
    }
    return p;
}
int main(){
    int T;
    cin >> T;
    for(int i=0; i<T; i++){
        int a;
        cin >> a;

        if(a>0){
            push(a);
        }
        if(a==0){
            if(heap_count == 0){
                cout << "0" << '\n';
            }
            else{
                cout << pop() << '\n';
            }
        }
    }
    
    return 0;
}