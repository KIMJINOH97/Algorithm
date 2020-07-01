#include <iostream>
#include <cmath>
#define max 100001
using namespace std;

int heap[max];
int h_count = 0;

void swap(int* a, int* b) {
	int temp = *a; *a = *b; *b = temp;
}

bool compare(int a, int b){
    if(abs(a) < abs(b)){
        return true;
    }
    else if(abs(a) == abs(b)){
        if(a<b){
            return true;
        }
        else{
            return false;
        }
    }
    else{
        return false;
    }
}

void push(int x) {
	heap[++h_count] = x;
	int child = h_count;
	int parent = child / 2;
	while (child > 1 && compare(heap[parent], heap[child]) == false){
        swap(&heap[parent], &heap[child]);
		child = parent;
		parent = child / 2;
	}
}

int pop() {
	int p = heap[1];
	swap(&heap[h_count], &heap[1]);
	h_count--;

	int parent = 1;
	int child = 2;
    if(child+1 <= h_count && compare(heap[child], heap[child+1])==false){
        child = child+1;
    }
	
	while (child <= h_count && compare(heap[parent], heap[child]) == false) {
        swap(&heap[parent], &heap[child]);
		parent = child;
		child = parent * 2;
        if (child + 1 <= h_count && compare(heap[child], heap[child+1]) == false){
            child = child +1;
        }
	}
	return p;
}

int main() {
	int T;
	cin >> T;
	while (T--) {
		int a;
		cin >> a;
		if (a != 0) {
			push(a);
		}
		else {
			if (h_count == 0) {
				cout << "0" << '\n';
			}
			else {
				cout << pop() << '\n';
			}
		}
	}
	return 0;
}