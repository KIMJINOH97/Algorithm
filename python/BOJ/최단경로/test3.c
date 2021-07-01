#include <stdio.h>

void f4(){}
void f3(){f4();}
void f2(){f3();f3();f3();f3();f3();}
void f1(){f2();f5();}
int f5(){return 100;}
int main(){
	int a = 10;
	char map[100-a][100+a][100+a*2];
	short visited[10] = {0,1,2,3,4,5,6,7,8,9};
	f1();
	int b = sizeof(a);
	float c;
	a = f5();
	c = (float)a;
	scanf("%lf",&c);
	printf("a's size : %d\n",b);
	for(a=0;a<-1;a++){
		printf("a");
	}
}
