%{
#include <string.h>
#include <math.h> 
static int size = 200;
static int count;
static float stack[200];

void clean();

static void push (float x) {
  if (++count<size) {
    stack[count]= x;
  }
  else {
    printf ("STACK IS FULL\n");
    }
}

static float pop (void) {
  if (count>=0) {
    return stack[count--];
  }
  else {
    printf ("Błąd: za mała liczba argumentów\n"); 
    clean();
    return;
  }
}

int int_v;
%}

digit [0-9]
int {digit}+
int2 [+-]{int}

%%

({int}|{int2})  {push (atof(yytext));}
"+" {push (pop() + pop());}
"*" {push (pop() * pop());}
"-" {int f= pop(); push ((int)pop() - f);}
"/" {int f= pop(); push ((int)pop() / f);}
"^" {int f= pop(); push (pow((int)pop(), f));}
"%" {int f= pop(); push ((int)pop() % f);}
\n  {int answer = pop(); if (count < 0) {printf("%d\n",answer);} else {printf ("Błąd: za mała liczba operatorów\n");}; clean();}
[^-0-9+*/ \t\n]+  {ECHO; fprintf (stderr,"Błąd: zły symbol"); printf("\n"); clean();} 
%%

int main () {
  count= -1;
  yylex();
  return 0;
  }

int yywrap () {
  return 1;
  }

void clean() {
  count= -1;
  yylex();
  return;
}