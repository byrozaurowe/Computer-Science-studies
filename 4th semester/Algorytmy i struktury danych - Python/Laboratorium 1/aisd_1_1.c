#include<stdio.h>

const int MAX = 1000;

void exception(char ex) {
	if (ex == 'f') {
		printf("Queue is full!\n");
	}
	if (ex == 'e') {
		printf("Queue is empty!\n");
	}
}

void push_back(int number, int tab[], int *end) {
	if ((*end) == MAX-1) {
		exception('f');
	}
	else {
		(*end)++;
		tab[(*end)] = number;
		printf("New number added on queue\n");
	}
}

void pop_back(int tab[], int *end) {
	if ((*end) == -1) {
		exception('e');
	}
	else {
		printf("First element was %d\n", tab[0]);
		for (int i=0; i<(*end); i++) {
			tab[i] = tab[i+1];
		}
		tab[(*end)] = 0;
		(*end)--;
	}
}

int main() {
	int tab[MAX];
	int end = -1;
	
	push_back(2, tab, &end);
	push_back(10, tab, &end);
	push_back(4, tab, &end);
	push_back(2, tab, &end);
	
	pop_back(tab, &end);
	pop_back(tab, &end);
	pop_back(tab, &end);
	pop_back(tab, &end);
	pop_back(tab, &end);
	
	for (int i=0; i <= MAX; i++) {
		push_back(2, tab, &end);
	}
	
	return 0;
}