all: lexer parser
	g++ parser.tab.c lex.yy.c -lfl -o calc

lexer:
	flex lexer.l

parser:
	bison -d parser.y