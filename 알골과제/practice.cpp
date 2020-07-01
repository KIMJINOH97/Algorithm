#include <iostream>
using namespace std;
struct BigInt {
   char digits[100];
   int ndigits;
};
// Converts digit strings into BigInt structures.
// e.g.) "123" ==> (digits = [3, 2, 1], ndigits = 3)
void convert(BigInt *p, char *s) {
   int n = 0;
   while (*s++ != '\0') // Find the end of
      n++;       //the string s
   *s--;
   p->ndigits = n;
   while (n >= 0)
   p->digits[n--] = *s--;
} 

// Prints BigInt structures.
// e.g.) For (digits = [3, 2, 1], ndigits = 3),
// it displays "123“
void print(BigInt x) {
   int n = x.ndigits;
   for(int i=0; i<=n; i++)
      cout << x.digits[i];
}
// Prints "a = 123456789123456789"
int main() {
   BigInt a;
   convert(&a, "123456789123456789");
   cout << "a = ";
   print(a);
   cout << endl;
   return 0;
}