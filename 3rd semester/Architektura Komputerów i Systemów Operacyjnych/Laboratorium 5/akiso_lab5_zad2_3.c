#include<stdio.h>
#include <signal.h>
#include <unistd.h>

void handle_sigint(int signal) {
	printf("\ncaught signal %d\n", signal);
	sleep(1);
}

int main() {
	signal(10, handle_sigint);
	while(1);
	return 0;
}

/* */