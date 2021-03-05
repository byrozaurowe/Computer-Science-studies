%{
#include<stdio.h>

int yylex();
int yywrap();

int words = 0;
int lines = 0;
%}

%%

^[ \t]*\n    ;
^[ \t]*     ;
[ \t]*\n { printf("\n"); lines++; }
[ \t]+  { printf(" "); }
[^ \t\n]+    { words++; ECHO; }

%%

int yywrap() {
    return 1;
}

int main(int argc, char* argv[]) {
    yylex();
    printf("\n words =  %d \n lines = %d\n", words, lines);

    return 0;
}