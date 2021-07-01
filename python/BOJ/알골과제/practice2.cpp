#include <iostream>
#include <cmath>

using namespace std;

int main(){
    float N;
    cin >> N;

    printf("nlog2(n) - (n-1) = %.3f \n", (float)(N*log2(N) -(N-1)));
    printf("(n+1)2ln(n) = %.3f \n", (float)((N+1)*2*log(N)));

    return 0;
}