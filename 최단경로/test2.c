#include <stdio.h>

unsigned int f1()
{
	printf("i am f1\n");
	return 1;
}
signed int f2(){return 1;}
double f3(){f1();return 1.1;}
int f4();
int main(){
	const int a = 4000;
	float b = 5.2324;
	char c = 'Z';
	long d = 041657;
	long e = -21556;
	int f = -185;
	short g = 0x30;
	short h = -130;
	double i = 4.1234567890;
	float j = -3.55; 
	if( a < b || b < d) {}
	switch(c){
		case 'Z':
		f3();
		break;
	}
	if ( 0 > 1){
		f3();
	}
	do{
		f3();
	}while(0> 1);
	while(0>1 && 0<1 || 1<2){
		f3();
	}
}
int f4(){
	return 1000;
}
