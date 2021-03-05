#include<stdio.h>
#include<stdlib.h>

typedef struct element {
	int value;
	struct element *next;
} element;

typedef struct list {
	element *first;
} list;

void constructList(list *thisList) {
	(*thisList).first = (element *)malloc(sizeof(element*));
	(*thisList).first = NULL;
}

void add(int value, list *thisList) {
	if ((*thisList).first == NULL) {
		(*thisList).first = (element *)malloc(sizeof(element*));
		((*thisList).first) -> value = value;
		((*thisList).first) -> next = NULL;
		printf("First element added on list\n");
	}
	else {
		element *tmp = (*thisList).first;
		while (tmp -> next != NULL) {
			tmp = tmp -> next;
		}
		tmp -> next = (element *)malloc(sizeof(element*));
		tmp -> next -> value = value;
		tmp -> next -> next = NULL;
		printf("Next element added on list\n");
	}
}

void rem(int num, list *thisList) {
	if ((*thisList).first == NULL) {
		printf("List is empty!\n");
	}
	else if (num == 1) {
		element *first = (*thisList).first;
		(*thisList).first = first -> next;
		free (first);
	}
	else if (num >= 2) {
		element *tmp = (*thisList).first;
		int i = 1;

		while (tmp) {
			if ((i+1) == num) break;

			tmp = tmp -> next;
			i++;
		}

		if (i+1 != num) {
			printf("List doesn't contain this element\n");
		}
		else {
			element *del = tmp -> next;
			tmp -> next = tmp -> next -> next;
			free (del);
		}
	}
}

void print(list *thisList) {
	if ((*thisList).first == 0) {
		printf ("List is empty!\n");
	}
	else {
		printf("Printing:\n");
		element *tmp = (*thisList).first;
		printf("%d\n", tmp -> value);
		while(tmp -> next != 0) {
			tmp = tmp -> next;
			int val = tmp -> value;
			printf("%d\n", val);
		} 
	}
}

int printElement(int num, list *thisList) {
	int time = clock();
	element *tmp = (*thisList).first;
	int i = 1;
	while (tmp)
	{
		if (i == num) break;
		tmp = tmp -> next;
		i++;
	}
	if (i != num) {
		printf("List doesn't contain this element\n");
		return 0;
	}
	else {
		printf("Value of element: %d\n", tmp -> value);
		time = clock() - time;
		printf("Access time: %ld\n", time);
		return time;
	}
}

void merge (list *firstList, list *secondList) {
	element *last = (*firstList).first;
	while (last -> next != NULL) {
		last = last -> next;
	}
	last -> next = (*secondList).first;
}

int main() {
	list list1;
	constructList(&list1);

	for (int i = 0; i < 1000; i++) {
		int num = rand();
		add(num, &list1);
	}
	
	float oneTime = 0;
	for (int i = 0; i <1000; i++) {
		oneTime += printElement(2, &list1);
	}
	oneTime /= 1000;

	float randomTime = 0;
	for (int i = 0; i <1000; i++) {
		int num = random()%1000+1;
		randomTime += printElement(num, &list1);
	}
	randomTime /= 1000;

	printf("Średni czas dostępu do jednego elementu: %f\n", oneTime);
	printf("Średni czas dostępu do losowego elementu: %f\n", randomTime);

	return 0;
}