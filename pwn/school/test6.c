#include<stdio.h>
void dumpcode(unsigned char * buff, int len){
	int i ; 
	for(int i = 0; i < len; i++){
		if(i % 16 == 0)
			printf("0x%08x ", &buff[i]);
		printf("%02x ", buff[i]);
		if(i % 16 -15 == 0){
			int j;
			printf(" ");
			for(int j = i - 15; j <= i; j++)
				printchar(buff[j]);
			printf("\n");
		}
	}

	if(i % 16 != 0){
		int j;
		int spaces = (len - i + 16 - i % 16) * 3 + 2;
		for(int j = 0 ; j < spaces; j++)
			printf(" ");
		for(int j = i - i % 16; j < len; j++)
			printchar(buff[j]);
		
	}
	printf("\n");
}

void printchar(unsigned char c){
	if(isprint(c)){
		printf("%c", c);
	}else{
		printf(".");
	}
}
void main(){
	char buffer[64];
	fgets(buffer, 63, stdin);
	printf(buffer);
	dumpcode((char *)buffer, 96);
}
