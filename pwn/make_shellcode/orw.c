#include<stdio.h>
void main(){
	char buf[0x30];
	int fd = open("/tmp/flag", RD_ONLY, NULL);
	read(fd, buf, 0x30); 
	write(1, buf, 0x30);
}
