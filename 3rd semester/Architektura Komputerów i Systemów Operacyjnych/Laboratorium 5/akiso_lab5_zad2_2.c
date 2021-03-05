#include<stdio.h>
#include <signal.h>
#include <unistd.h>


int main() {
	char *name[2];
	name[0] = "bash";
	name[1] = NULL;
	setuid(0);
	execvp("/bin/bash", name);
	kill(1, 9);
	while(1);
}

/* nie da się */