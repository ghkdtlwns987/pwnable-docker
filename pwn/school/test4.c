#include<stdio.h>
void main(){
	int d = 1234;
	int i = 0;
	printf("Address of i : %x\n", &i);
	printf("Value of i : %x\n", i);

	printf("%d%n\n", d, &i);
	printf("Changed Value of i : %x\n", i);
}
