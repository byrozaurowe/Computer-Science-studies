 
%option noyywrap
%{
#include "parser.tab.h"
#include<stdio.h>
int yylex();
%}

%x COMMENT

%%
^#(.|\\\n)*\n                   ;
\n                              { return NEWLINE; }
[0-9]+                          { yylval = atoi(yytext); return NUM; }
\+                              { return PLUS; }
\-                              { return MINUS; }
\*                              { return MULT; }
\/                              { return DIV; }
\^                              { return PWR; }
\(                              { return LEFTBRACKET; }
\)                              { return RIGHTBRACKET; }
.                               ;
%%
