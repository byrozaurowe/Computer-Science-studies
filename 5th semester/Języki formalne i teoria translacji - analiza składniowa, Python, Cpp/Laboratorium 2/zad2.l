%{
#include<stdio.h>
#include<stdbool.h>

int yylex();
int yywrap();

bool start_comment = true;
void comment_finished() {
	start_comment = false;
}
%}

%x one_apostrophe
%x two_apostrophe
%x three_apostrophe
%x three_double

%%

#!.*\n  {if(start_comment) {ECHO; comment_finished();};};
<INITIAL>[\'] {printf("%s", yytext); BEGIN(one_apostrophe);};
<one_apostrophe>[^\\]"\\\\"*[\']    {printf("%s", yytext); BEGIN(0);};
<INITIAL>[\"] {printf("%s", yytext); BEGIN(two_apostrophe);};
<two_apostrophe>[^\\]"\\\\"*[\"]    {printf("%s", yytext); BEGIN(0);};
<INITIAL>"\'\'\'" {printf("%s", yytext); BEGIN(three_apostrophe);};
<three_apostrophe>[^\\]"\\\\"*"\'\'\'"    {printf("%s", yytext); BEGIN(0);};
<INITIAL>"\"\"\"" {printf("%s", yytext); BEGIN(three_double);};
<three_double>[^\\]"\\\\"*"\"\"\""    {printf("%s", yytext); BEGIN(0);};
"^#.*\n?"  {};
#.*\n?  {printf("\n"); };

%%

int yywrap() {
    return 1;
}

int main(int argc, char* argv[]) {
    yylex();
    printf("\n");

    return 0;
}