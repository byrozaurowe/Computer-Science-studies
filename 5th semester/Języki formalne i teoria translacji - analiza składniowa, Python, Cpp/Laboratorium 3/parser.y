%{
#define YYSTYPE int
#include<stdio.h>
#include<iostream>
#include<cstring>
#include<cmath>
using namespace std;

int yylex();
void yyerror(string);
bool err = false;
string onp = "";

int z(int x);
int multiply(int a, int b);

int divide(int a, int b) {
    int Z = 1234577;
    int m = Z;
    int x = 1;
    int y = 0;

    while(b > 1) {
        int i = b/m;
        int t = m;
        m = b % m;
        b = t;
        t = y;

        y = x - i * y;
        x = t;
    }
    if (x < 0) {
        x += Z;
    }
    return z(multiply(a, x));
}

int multiply(int a, int b) {
    int x = 0;
    int Z = 1234577;
    for (int i = 0; i < b; i++) {
        x = (x + a) % Z;
    }
    return x;
}

int power(int a, int b) {
    int res = 1;
    for (int i = 0; i < b; i++) {
        res = res * a;
        res = res % 1234577;
    }
    return res;
}

int z(int x) {
    int Z = 1234577;
    return ((x % Z) + Z) % Z;
}
%}

%token NUM
%token ERROR
%token NEWLINE
%token LEFTBRACKET
%token RIGHTBRACKET
%left PLUS MINUS
%left MULT DIV
%right PWR
%precedence NEG

%%
input:
    %empty
    | input line
;

line:
    NEWLINE | expr NEWLINE   {
                        cout << onp << endl;
                        if (!err) {
                            cout << "Wynik: " << z($1) << endl;
                            err = false;
                            onp = "";
                        }
                    }
    | error NEWLINE {
                        cout << "BŁĄD"  << endl;
                        err = false;
                        onp = "";
                    }
;

expr:
    NUM                         { $$ = z($1); onp.append(to_string($1)).append(" "); }
    | expr PLUS expr            { $$ = ($1 + $3)%1234577; onp.append("+ "); }
    | expr MINUS expr           { $$ = ($1 - $3)%1234577; onp.append("- "); }
    | expr MULT expr            { $$ = multiply($1, $3); onp.append("* "); }
    | expr DIV expr             { 
                                    onp.append("/ ");
                                    if($3 == 0) {
                                        yyerror("dzielenie przez 0");
                                    }
                                    else {
                                        $$ = divide($1, $3);
                                    }
                                }
    | MINUS expr %prec NEG  { 
                                    $$ = z(-$2);
                                    onp = onp.substr(0, onp.find_last_of(' '));
                                    onp = onp.substr(0, onp.find_last_of(' ')+1);
                                    onp.append(to_string(z(-$2))).append(" ");
                                }
    | expr PWR expr             {
                                    onp.append("^ ");
                                    $$ = power($1, $3);
                                }
    | LEFTBRACKET expr RIGHTBRACKET   { $$ = z($2); }
;

%%

void yyerror(string err_msg) {
    cout << "Error: " << err_msg << endl;
    err = true;
    return;
}

int main() {
    return yyparse();
}