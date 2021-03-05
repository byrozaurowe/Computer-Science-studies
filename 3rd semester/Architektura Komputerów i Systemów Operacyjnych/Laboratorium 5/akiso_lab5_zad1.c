#include<stdio.h>

int main() {
	char *name[2];
	name[0] = "bash";
	name[1] = NULL;
	setuid(0);
	execvp("/bin/bash",name);
}

/* przed uruchomieniem nalezy nadac uprawnienia
sudo chown root:root akiso_lab5_zad1
sudo chmod 4755 akiso_lab5_zad1 */