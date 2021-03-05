%{
#include<stdio.h>
#include <stdbool.h>
#include<string.h>

int yylex();
int yywrap();

bool preserve_doc = true;
%}

%x string_mode
%x documentation
%x long_comment
%x ESCAPE

%%
\\												{ECHO; BEGIN(ESCAPE); };
<ESCAPE>.										{ECHO; BEGIN(0); };

.?\"\"											{ECHO;};

\n?[[:blank:]]*((\/\/\/)|(\/\/!)).*(\\\n.*)*	{if(preserve_doc) ECHO;};

\n?[[:blank:]]*\/\/.*(\\\n.*)*					{};
\/\/.*(\\\n.*)*									{};

(^[[:blank:]]*)?(\/\*\*)|(\/\*\!)				{if(preserve_doc) ECHO; BEGIN(documentation); };
<documentation>\/*\**							{if(preserve_doc) ECHO;};
<documentation>[^\*\/]*							{if(preserve_doc) ECHO;};
<documentation>(\*\/)							{if(preserve_doc) ECHO; BEGIN(0); };

(^[[:blank:]]*)?\/\*							{BEGIN(long_comment); };
<long_comment>\/*\**							{};
<long_comment>[^\*\/]*							{};
<long_comment>\*\/[[:blank:]]*\n?				{BEGIN(0); };

[\"]											{ECHO; BEGIN(string_mode); };
<string_mode>[^\\][\"]							{ECHO; BEGIN(0); };
<string_mode>[^\\]"\\\\"+[\"]				{ECHO; BEGIN(0); };


%%

int yywrap() {
    return 1;
}

int main(int argc, char* argv[]) {
    if (argc > 1) {
        if (strcmp(argv[1], "--doc") == 0) {
            preserve_doc = false;
        }
    }
    yylex();
    printf("\n");

    return 0;
}