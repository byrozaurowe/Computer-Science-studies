#include<stdio.h>
#include<stdlib.h>

typedef struct element {
	int value;
	struct element *next;
    struct element *prev;
} element;

typedef struct list {
	element *first;
    int size;
} list;

void constructList(list *thisList) {
	(*thisList).first = (element *)malloc(sizeof(element*));
	(*thisList).first = NULL;
    (*thisList).size = 0;
}

void add(int value, list *thisList) {
	if ((*thisList).first == NULL) {
		(*thisList).first = (element *)malloc(sizeof(element*));
		((*thisList).first) -> value = value;
		((*thisList).first) -> next = ((*thisList).first);
        ((*thisList).first) -> prev = ((*thisList).first);

        (*thisList).size++;
		printf("First element added on list\n");
	}
    else {
		element *tmp = (*thisList).first;
		while (tmp -> next != (*thisList).first) {
			tmp = tmp -> next;
		}
		tmp -> next = (element *)malloc(sizeof(element*));
		tmp -> next -> value = value;
		tmp -> next -> next = ((*thisList).first);
		tmp -> next -> prev = tmp;
		((*thisList).first) -> prev = tmp -> next;
		(*thisList).size++;
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
		(*thisList).first -> prev = first -> prev;
		first -> prev -> next = (*thisList).first;
		free (first);

        (*thisList).size--;
        printf("Removed first element\n");
	}
	else if (1 < num && num <= (*thisList).size) {
		element *tmp = (*thisList).first;
		int i = 1;

		while (i <= (*thisList).size) {
			if ((i+1) == num) break;

			tmp = tmp -> next;
			i++;
		}
		element *del = tmp -> next;
		tmp -> next = del -> next;
		tmp -> next -> prev = tmp;
		free (del);

        (*thisList).size--;
        printf("Removed middle or last element\n");
	}
    else printf("List doesn't contain thist element\n");
}

void print(list *thisList) {
	if ((*thisList).first == 0) {
		printf ("List is empty!\n");
	}
	else {
		printf("Printing:\n");
		element *tmp = (*thisList).first;
		printf("Element: %d\n", tmp -> value);
        int i = 1;
		while(tmp -> next != (*thisList).first) {
			tmp = tmp -> next;
			int val = tmp -> value;
			printf("Element: %d\n", val);
		} 
	}
}

int printElement(int num, list *thisList) {
	int time = clock();
		if (num <= (*thisList).size/2) {
			element *tmp = (*thisList).first;
			int i = 1;
			while (tmp) {
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
		if (num > (*thisList).size/2) {
			element *tmp = (*thisList).first;
			int i = (*thisList).size + 1;
			while (tmp) {
				if (i == num) break;
				tmp = tmp -> prev;
				i--;
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
}

void merge (list *firstList, list *secondList) {
	element *last = (*firstList).first -> prev;
	element *secondLast = (*secondList).first -> prev;
	last -> next = (*secondList).first;
	(*secondList).first -> prev = last;
	(*firstList).first -> prev = secondLast;
	secondLast -> next = (*firstList).first;
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
		oneTime += printElement(500, &list1);
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