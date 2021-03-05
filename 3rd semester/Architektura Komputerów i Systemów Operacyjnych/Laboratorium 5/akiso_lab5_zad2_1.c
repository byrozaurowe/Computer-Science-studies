#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void handle_sigint(int signal) {
	printf("\ncaught signal %d\n", signal);
}

int main() {
	for (int i=0; i<64; i++) {
		signal(i+1, handle_sigint);
		kill(getpid(), i+1);
	}
	while(1);
	return 0;
}
/* nie da się obsłużyć wszystkich procesów, np 9 - kill */