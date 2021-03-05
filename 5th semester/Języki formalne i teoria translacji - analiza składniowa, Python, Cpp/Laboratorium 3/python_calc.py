import ply.yacc as yacc
import ply.lex as lex
from sys import stdin

def z(x):
    Z:int = 1234577
    return ((x % Z) + Z) % Z

def multiply(a:int, b:int):
    x:int = 0
    Z:int = 1234577
    for i in range (int(b)):
        x = (x + a) % Z
    return z(x)

def divide(a:int, b:int):
    Z:int = 1234577
    m:int = Z
    x:int = 1
    y:int = 0

    while b > 1:
        i:int = int(b/m)
        t:int = m
        m = b % m
        b = t
        t = y

        y = int(x - i * y)
        x = t
    if x < 0:
        x += Z
    return z(multiply(a, x))

def power(a:int, b:int):
    res:int = 1
    Z:int = 1234577
    for i in range(b):
        res = res * a
        res = res % Z
    return z(res)

tokens = ('NEWLINE', 'COM', 'NUM', 'LEFTBRACKET', 'RIGHTBRACKET', 'PLUS', 'MINUS', 'MULT', 'DIV', 'PWR')

t_COM = r'\#.*'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'\/'
t_PWR = r'\^'
t_LEFTBRACKET = r'\('
t_RIGHTBRACKET = r'\)'
t_NEWLINE = r'\n+'

def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_error(t):
    t.lexer.skip(1)

lex.lex()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV'),
    ('right', 'NEG', 'PWR')
)

def p_STAR_EXPR(p):
    'STAR : EXPR'
    print()
    print('Wynik:', p[1])

def p_STAR_COM(p):
    'STAR : COM'
    pass

def p_NUMR(p):
    'NUMR : NUM'
    p[0] = z(p[1])
    print(p[0], '', end='')

def p_NUMR_NEG(p):
    'NUMR : MINUS NUM %prec NEG'
    p[0] = z(0 - p[2])
    print(p[0], '', end='')

def p_EXPR_PLUS(p):
    'EXPR : EXPR PLUS EXPR'
    p[0] = z(p[1] + p[3])
    print('+ ', end='')

def p_EXPR_MINUS(p):
    'EXPR : EXPR MINUS EXPR'
    p[0] = z(p[1] - p[3])
    print('- ', end='')

def p_EXPR_MULT(p):
    'EXPR : EXPR MULT EXPR'
    p[0] = multiply(p[1], p[3])
    print('* ', end='')

def p_EXPR_DIV(p):
    'EXPR : EXPR DIV EXPR'
    x = p[1]
    y = p[3]
    if y == 0:
        raise 'dzielenie przez 0'
    p[0] = divide(x, y)
    print('/ ', end='')

def p_EXPR_PWR(p):
    'EXPR : NUMR PWR NUMR'
    p[0] = power(p[1], p[3])
    print('^ ', end='')

def p_EXPR_BRACKETS(p):
    'EXPR : LEFTBRACKET EXPR RIGHTBRACKET'
    p[0] = p[2]    

def p_EXPR_NUM(p):
    'EXPR : NUMR'
    p[0] = p[1]

def p_error(p):
    if p != None:
        print(f'\nBŁĄD: ‘{p.value}’')
    else:
        print(f'BŁĄD')

yacc.yacc()

while(1):
    line = str(input())
    if line[-2] == '\\':
        line += str(input())
    yacc.parse(line)