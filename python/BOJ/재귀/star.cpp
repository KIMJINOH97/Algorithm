#include <iostream>

using namespace std;
int N;
void star(int N){
    if(N==1)
        return ;
    if(N%3 == 0)
    for(int i=0; i<N/3;i++)
        cout << "***";
    for(int i=0; i<N/3; i++)
        cout << "* *";
    for(int i=0; i<N/3; i++)
        cout << "***";

}

int main(){
    cin >> N;
    star(N);

    return 0;
}