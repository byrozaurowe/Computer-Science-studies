# Wiktoria Byra 250131, Języki formalne i teoria translacji, projekt kompilatora, 2021

import ply.lex as lex
from ply.lex import TOKEN

reserved = {
    'DECLARE': 'DECLARE',
    'BEGIN': 'BEGIN',
    'IF': 'IF',
    'THEN': 'THEN',
    'ELSE': 'ELSE',
    'ENDIF': 'ENDIF',
    'WHILE': 'WHILE',
    'ENDWHILE': 'ENDWHILE',
    'REPEAT': 'REPEAT',
    'UNTIL': 'UNTIL',
    'FOR': 'FOR',
    'FROM': 'FROM',
    'TO': 'TO',
    'DOWNTO': 'DOWNTO',
    'ENDFOR': 'ENDFOR',
    'READ': 'READ',
    'WRITE': 'WRITE',
}

tokens = [
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULO',
    'EQU',
    'INEQU',
    'LOWERTHAN',
    'GREATERTHAN',
    'LOWEREQU',
    'GREATEREQU',
    'LPAREN',
    'RPAREN',
    'SEMI',
    'COLON',
    'COMMA',
    'ASSIGN',
    'END',
    'DO',
    'num',
    'pidentifier'
] + list(reserved.values())

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_MODULO = r'\%'
t_EQU = r'\='
t_INEQU = r'!='
t_LOWERTHAN = r'<'
t_GREATERTHAN = r'>'
t_LOWEREQU = r'<='
t_GREATEREQU = r'>='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'
t_COLON = r':'
t_COMMA = r','
t_ASSIGN = r':='
t_END = r'END'
t_pidentifier = r'[_a-z]+'
t_DO = r'DO'


def t_COMMENT(t):
    r'\[(.|\n)*?\]'
    pass


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_num(t):
    r'\d+'
    t.value = abs(int(t.value))
    return t


def t_error(t):
    raise Exception("Błędny znak '%s' w linii %i" % (t.value[0], t.lineno))


reserved_re = '|'.join(reserved.values())
@TOKEN(reserved_re)
def t_CONTROL(t):
    controlToken = reserved.get(t.value)
    if(not controlToken):
        raise SyntaxError("Błędna sekwencja '%s'" % t.value)
    t.type = controlToken
    return t


lexer = lex.lex()