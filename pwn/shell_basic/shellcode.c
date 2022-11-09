#include<stdio.h>
void main(){
	char buf[0x30];
	//int fd = open("/home/shell_basic/flag_name_is_loooooong", 0, NULL);
	int fd = open("./flag", 0, NULL);
	read(fd, buf, 0x30); 
	write(1, buf, 0x30);
}
