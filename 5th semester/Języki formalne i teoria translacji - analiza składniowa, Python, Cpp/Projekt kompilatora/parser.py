# Wiktoria Byra 250131, Języki formalne i teoria translacji, projekt kompilatora, 2021

from tokenizer import lexer, tokens
from program import Program
import ply.yacc as yacc
from condition import Condition
from expression import ValueFromIdentifier, Number, Expression, Operator
from identifier import Identifier, ArrayAccessByNum, ArrayAccessByPidentifier
from command import *
from declaration import *


def p_program(p):
    '''program  : DECLARE declarations BEGIN commands END'''
    p[0] = Program(p[4], p[2])


def p_program_NO_DECLARATION(p):
    '''program  : BEGIN commands END'''
    p[0] = Program(p[2])


def p_declarations_VARIABLE(p):
    '''declarations : declarations COMMA pidentifier'''
    if not p[1]:
        p[1] = []
    newVariable = VariableDeclaration(p[3], lineNumber=p.lineno(2))
    p[1].append(newVariable)
    p[0] = p[1]


def p_declarations_ARRAY(p):
    '''declarations : declarations COMMA pidentifier LPAREN num COLON num RPAREN'''
    if not p[1]:
        p[1] = []
    rangeFrom = p[5]
    rangeTo = p[7]
    pidentifier = p[3]
    newArray = ArrayDeclaration(pidentifier, rangeFrom, rangeTo, line=p.lineno(2))
    p[1].append(newArray)
    p[0] = p[1]


def p_declarations_LAST_VARIABLE(p):
    '''declarations : declarations pidentifier'''
    if not p[1]:
        p[1] = []
    newVariable = VariableDeclaration(p[2], lineNumber=p.lineno(2))
    p[1].append(newVariable)
    p[0] = p[1]


def p_declarations_LAST_ARRAY(p):
    '''declarations : declarations pidentifier LPAREN num COLON num RPAREN'''
    if not p[1]:
        p[1] = []
    rangeFrom = p[4]
    rangeTo = p[6]
    pidentifier = p[2]
    newArray = ArrayDeclaration(pidentifier, rangeFrom, rangeTo, line=p.lineno(2))
    p[1].append(newArray)
    p[0] = p[1]


def p_declarations_EMPTY(p):
    '''declarations : '''
    p[0] = []


def p_commands_more(p):
    '''commands  : commands command'''
    if not p[1]:
        p[1] = []
    p[1].append(p[2])
    p[0] = p[1]


def p_commands(p):
    '''commands  : command'''
    p[0] = [p[1]]


def p_command_ASSIGN(p):
    '''command  : identifier ASSIGN expression SEMI'''
    p[0] = CommandAssign(p[1], p[3], line=p.lineno(2))


def p_command_IFTHENELSE(p):
    '''command  : IF condition THEN commands ELSE commands ENDIF'''
    p[0] = CommandIfThenElse(p[2], p[4], p[6])


def p_command_IFTHEN(p):
    '''command  : IF condition THEN commands ENDIF'''
    p[0] = CommandIfThen(p[2], p[4])


def p_command_WHILE(p):
    '''command  : WHILE condition DO commands ENDWHILE'''
    p[0] = CommandWhile(p[2], p[4])


def p_command_REPEATUNTIL(p):
    '''command  : REPEAT commands UNTIL condition SEMI'''
    p[0] = CommandRepeatUntil(p[2], p[4])


def p_command_FOR(p):
    '''command  : FOR pidentifier FROM value TO value DO commands ENDFOR'''
    p[0] = CommandForTo(p[2], p[4], p[6], p[8], p.lineno(1))


def p_command_FORDOWNTO(p):
    '''command  : FOR pidentifier FROM value DOWNTO value DO commands ENDFOR'''
    p[0] = CommandForDownto(p[2], p[4], p[6], p[8])


def p_command_READ(p):
    '''command  : READ identifier SEMI'''
    p[0] = CommandRead(p[2])


def p_command_WRITE(p):
    '''command  : WRITE value SEMI'''
    p[0] = CommandWrite(p[2])


def p_expression_value(p):
    '''expression  : value'''
    p[0] = p[1]


def p_expression(p):
    '''expression   : value PLUS value
                    | value MINUS value
                    | value MULTIPLY value
                    | value DIVIDE value
                    | value MODULO value'''
    p[0] = Operator(left=p[1], operator=p[2], right=p[3])


def p_condition(p):
    '''condition    : value EQU value
                    | value INEQU value
                    | value LOWERTHAN value
                    | value GREATERTHAN value
                    | value LOWEREQU value
                    | value GREATEREQU value'''
    p[0] = Condition(left=p[1], operator=p[2], right=p[3])


def p_value_identifier(p):
    '''value    : identifier'''
    p[0] = ValueFromIdentifier(p[1], lineNumber=p.lineno(1))


def p_value_num(p):
    '''value    : num'''
    p[0] = Number(p[1])


def p_identifier(p):
    '''identifier   : pidentifier'''
    p[0] = Identifier(p[1])


def p_identifier_arrayAccess_pidentifier(p):
    '''identifier   : pidentifier LPAREN pidentifier RPAREN'''
    p[0] = ArrayAccessByPidentifier(p[1], p[3])


def p_identifier_arrayAccess_num(p):
    '''identifier   : pidentifier LPAREN num RPAREN'''
    p[0] = ArrayAccessByNum(p[1], p[3])


def p_error(p):
    raise SyntaxError("Błędny znak '%s' w linii %i" % (p.value, p.lineno))


parser = yacc.yacc()