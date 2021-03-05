# Wiktoria Byra 250131, Języki formalne i teoria translacji, projekt kompilatora, 2021

from register import Register
from command import CommandForTo
from identifier import ArrayAccess
from memory import manager as Memory
from expression import Number


# instrukcje maszynowe
def GET(p, X):
    p.makeInstruction('GET', X)


def PUT(p, X):
    p.makeInstruction('PUT', X)


def STORE(p, reg, Y):
    p.makeInstruction('STORE', reg, Y)


def LOAD(p, reg, Y):
    p.makeInstruction('LOAD', reg, Y)


def INC(p, reg):
    p.makeInstruction('INC', reg)


def DEC(p, X):
    p.makeInstruction('DEC', X)


# rejestr/2
def SHR(p, X):
    p.makeInstruction('SHR', X)


# rejestr*2
def SHL(p, X):
    p.makeInstruction('SHL', X)    


def SUB(p, X, Y):
    p.makeInstruction('SUB', X, Y)


def ADD(p, X, Y):
    p.makeInstruction('ADD', X, Y)


def RESET(p, reg):
    p.makeInstruction('RESET', reg)


def READ(p, identifier):
    identifier.memoryAddressToRegister(p, Register.A, Register.B)
    Memory.initialize(identifier.pidentifier)
    GET(p, Register.A)


def WRITE(p, value):
    value.memoryAddressToRegisterInstruction(p, Register.B)
    PUT(p, Register.B)


def JUMP(p, j):
    p.makeInstruction('JUMP', j)


def JZERO(p, X, j):
    p.makeInstruction('JZERO', X, j)


def JODD(p, X, j):
    p.makeInstruction('JODD', X, j)


# jumpy do wykonania po zliczeniu linii kodu
class Future:
    # wykonaj
    def materialize(self, j):
        raise Exception("Funkcja materialize() niezdefiniowana dla %s" % self.__class__)


class FutureJZERO(Future):
    def __init__(self, program, X):
        self.X = X
        self.program = program
        self.instrId = program.addFutureInstruction(self)

    def materialize(self, j):
        self.program.instructions[self.instrId] = "%s %s %s" % (
            'JZERO', self.X, j)


class FutureJODD(Future):
    def __init__(self, program, X):
        self.X = X
        self.program = program
        self.instrId = program.addFutureInstruction(self)

    def materialize(self, j):
        self.program.instructions[self.instrId] = "%s %s %s" % (
            'JODD', self.X, j)


class FutureJUMP(Future):
    def __init__(self, program):
        self.program = program
        self.instrId = program.addFutureInstruction(self)

    def materialize(self, j):
        self.program.instructions[self.instrId] = "%s %s" % ('JUMP', j)


# funkcja ustawiająca daną wartość w rejestrze
def setRegisterConst(p, reg, val):
    RESET(p, reg)

    # korzystamy z zapisu binarnego liczby
    binVal = bin(val)[2:]
    length = len(binVal)
    for i, digit in enumerate(binVal):
        if digit == '1':
            INC(p, reg)
        if i < length - 1:
            SHL(p, reg)


# skopiowanie wartości z jednego rejestru do drugiego
def copy(p, X, Y):
    RESET(p, X)
    ADD(p, X, Y)


def ASSIGN(p, identifier, expression):
    decl = identifier.declaration
    if decl.islocal:
        raise Exception("Próba zmodyfikowania lokalnej zmiennej '%s'" % decl.pidentifier)
    if not isinstance(identifier, ArrayAccess) and decl.isarr == True:
        raise Exception("Niewłaściwe użycie zmiennej tablicowej '%s'" % decl.pidentifier)
    expression.evalueToRegisterInstruction(p, Register.B)
    identifier.memoryAddressToRegister(p, Register.A, Register.C)
    Memory.initialize(identifier.pidentifier)
    STORE(p, Register.B, Register.A)


# załadowanie wartości zmiennej w pamięci do rejestru
def LOAD_IDENTIFIER_VALUE_TO_REGISTER(p, identifier, reg):
    decl = identifier.declaration
    if reg == Register.E:
        raise Exception("Kolizja rejestrów '%s'" % reg)
    if decl.isarr == True:
        raise Exception("Niewłaściwe użycie zmiennej tablicowej '%s'" % decl.pidentifier)
    identifier.memoryAddressToRegister(p, Register.E, reg)
    LOAD(p, reg, Register.E)


# załadowanie adresu zmiennej w pamięci do rejestru
def LOAD_IDENTIFIER_MEMADDR_TO_REGISTER(p, identifier, reg):
    decl = identifier.declaration
    if reg == Register.E:
        raise Exception("Kolizja rejestrów '%s'" % reg)
    if decl.isarr == True:
        raise Exception("Niewłaściwe użycie zmiennej tablicowej '%s'" % decl.pidentifier)
    identifier.memoryAddressToRegister(p, reg, Register.E)


# załadowanie wartości z tablicy do rejestru
def LOAD_ARRAY_VALUE_TO_REGISTER(p, identifier, reg):
    identifier.memoryAddressToRegister(p, Register.A, reg)
    LOAD(p, reg, Register.A)


# załadowanie adresu tablicy do rejestru
def LOAD_ARRAY_MEMADDR_TO_REGISTER(p, identifier, reg):
    identifier.memoryAddressToRegister(p, reg, Register.A)


# załadowanie danej wartości do rejestru
def LOAD_NUMBER_VALUE_TO_REGISTER(p, number, reg):
    setRegisterConst(p, reg, number)


# przydzielenie danej wartości komórki w pamięci i załadowanie jej adresu do rejestru
def LOAD_NUMBER_MEMADDR_TO_REGISTER(p, number, reg):
    setRegisterConst(p, Register.F, number)
    rangeToValueMemBlockCopy = Memory.getUnnamedMemoryBlock()
    setRegisterConst(p, reg, rangeToValueMemBlockCopy)
    STORE(p, Register.F, reg)


def PLUS(p, leftValue, rightValue, destReg=Register.B, helpReg=Register.C):
    if destReg == helpReg:
        raise Exception("Nie można użyć tych samych rejestrów")
    leftValue.evalueToRegisterInstruction(p, destReg)
    rightValue.evalueToRegisterInstruction(p, helpReg)
    ADD(p, destReg, helpReg)
    # wynik dodawania w Register.B


def MINUS(p, leftValue, rightValue, destReg=Register.B, helpReg=Register.C):
    if destReg == helpReg:
        raise Exception("Nie można użyć tych samych rejestrów")
    leftValue.evalueToRegisterInstruction(p, destReg)
    rightValue.evalueToRegisterInstruction(p, helpReg)
    SUB(p, destReg, helpReg)
    # wynik odejmowania w Register.B


def MULTIPLY(p, leftValue, rightValue, destReg=Register.B, leftReg=Register.C, rightReg=Register.D):
    leftValue.evalueToRegisterInstruction(p, leftReg)
    rightValue.evalueToRegisterInstruction(p, rightReg)

    # zamiana czynników mnożenia w celu optymalizacji
    copy(p, destReg, leftReg)
    SUB(p, destReg, rightReg)
    fJUMP_SWAP = FutureJZERO(p, destReg)
    LABEL_JUMP_SWAP = p.getCounter()
    copy(p, destReg, rightReg)
    copy(p, rightReg, leftReg)
    copy(p, leftReg, destReg)
    LABEL_AFTER_SWAP = p.getCounter()
    fJUMP_SWAP.materialize(LABEL_AFTER_SWAP - LABEL_JUMP_SWAP + 1)

    # mnożenie
    RESET(p, destReg)
    LABEL3 = p.getCounter()
    fJZERO = FutureJZERO(p, leftReg)
    LABEL_JZERO = p.getCounter()
    fJODD = FutureJODD(p, leftReg)
    LABEL_JODD = p.getCounter()
    fJUMP = FutureJUMP(p)
    LABEL_JUMP = p.getCounter()
    ADD(p, destReg, rightReg)
    LABEL1 = p.getCounter()
    SHR(p, leftReg)
    SHL(p, rightReg)
    fJUMP2 = FutureJUMP(p)
    LABEL_JUMP2 = p.getCounter()

    # wykonanie jumpów
    fJZERO.materialize(LABEL_JUMP2 - LABEL_JZERO + 1)
    fJODD.materialize(LABEL_JUMP - LABEL_JODD + 1)
    fJUMP.materialize(LABEL1 - LABEL_JUMP + 1)
    fJUMP2.materialize(LABEL3 - LABEL_JUMP2 + 1)
    # wynik mnożenia w Register.B


def DIVIDE(p, numeratorVal, denominatorVal, destReg=Register.B, rightReg=Register.C):
    # czy dzielenie przez zero
    zero = Number(0)
    CONDITION_INEQU(p, denominatorVal, zero)
    fJZERO_NOT_ZERO = FutureJZERO(p, Register.B)
    LABEL_JUMP_NOT_ZERO = p.getCounter()
    RESET(p, destReg)
    fJZERO_ZERO = FutureJZERO(p, rightReg)
    LABEL_JZERO_ZERO = p.getCounter()

    # dzielenie
    numeratorVal.evalueToRegisterInstruction(p, destReg)
    denominatorVal.evalueToRegisterInstruction(p, rightReg)
    fJZERO = FutureJZERO(p, rightReg)
    LABEL_JZERO = p.getCounter()
    RESET(p, Register.D)
    INC(p, Register.D)
    LABEL0 = p.getCounter()
    copy(p, Register.A, destReg)
    SUB(p, Register.A, rightReg)
    fJZERO2 = FutureJZERO(p, Register.A)
    LABEL_JZERO2 = p.getCounter()
    SHL(p, rightReg)
    SHL(p, Register.D)
    fJUMP = FutureJUMP(p)
    LABEL_JUMP = p.getCounter()
    copy(p, Register.E, destReg)
    RESET(p, destReg)
    LABEL2 = p.getCounter()
    copy(p, Register.A, rightReg)
    SUB(p, Register.A, Register.E)
    fJZERO3 = FutureJZERO(p, Register.A)
    LABEL_JZERO3 = p.getCounter()
    fJUMP2 = FutureJUMP(p)
    LABEL_JUMP2 = p.getCounter()
    SUB(p, Register.E, rightReg)
    ADD(p, destReg, Register.D)
    LABEL3 = p.getCounter()
    SHR(p, rightReg)
    SHR(p, Register.D)
    fJZERO4 = FutureJZERO(p, Register.D)
    LABEL_JZERO4 = p.getCounter()
    fJUMP3 = FutureJUMP(p)
    LABEL_JUMP3 = p.getCounter()
    RESET(p, destReg)
    LABEL4 = p.getCounter()

    # wykonanie jumpów
    fJZERO_NOT_ZERO.materialize(LABEL_JZERO_ZERO - LABEL_JUMP_NOT_ZERO + 1)
    fJZERO_ZERO.materialize(LABEL4 - LABEL_JZERO_ZERO + 1)
    fJZERO.materialize(LABEL_JUMP3 - LABEL_JZERO + 1)
    fJZERO2.materialize(LABEL_JUMP - LABEL_JZERO2 + 1)
    fJUMP.materialize(LABEL0 - LABEL_JUMP + 1)
    fJZERO3.materialize(LABEL_JUMP2 - LABEL_JZERO3 + 1)
    fJUMP2.materialize(LABEL3 - LABEL_JUMP2 + 1)
    fJZERO4.materialize(LABEL4 - LABEL_JZERO4 + 1)
    fJUMP3.materialize(LABEL2 - LABEL_JUMP3 + 1)
    # wynik dzielenia w Register.B


def MODULO(p, numeratorVal, denominatorVal, destReg=Register.B, rightReg=Register.C):
    # czy dzielenie przez zero
    zero = Number(0)
    CONDITION_INEQU(p, denominatorVal, zero)
    fJZERO_NOT_ZERO = FutureJZERO(p, Register.B)
    LABEL_JUMP_NOT_ZERO = p.getCounter()
    RESET(p, destReg)
    fJZERO_ZERO = FutureJZERO(p, rightReg)
    LABEL_JZERO_ZERO = p.getCounter()

    # dzielenie
    numeratorVal.evalueToRegisterInstruction(p, destReg)
    denominatorVal.evalueToRegisterInstruction(p, rightReg)
    fJZERO = FutureJZERO(p, rightReg)
    LABEL_JZERO = p.getCounter()
    RESET(p, Register.D)
    INC(p, Register.D)
    LABEL0 = p.getCounter()
    copy(p, Register.A, destReg)
    SUB(p, Register.A, rightReg)
    fJZERO2 = FutureJZERO(p, Register.A)
    LABEL_JZERO2 = p.getCounter()
    SHL(p, rightReg)
    SHL(p, Register.D)
    fJUMP = FutureJUMP(p)
    LABEL_JUMP = p.getCounter()
    copy(p, Register.E, destReg)
    RESET(p, destReg)
    LABEL2 = p.getCounter()
    copy(p, Register.A, rightReg)
    SUB(p, Register.A, Register.E)
    fJZERO3 = FutureJZERO(p, Register.A)
    LABEL_JZERO3 = p.getCounter()
    fJUMP2 = FutureJUMP(p)
    LABEL_JUMP2 = p.getCounter()
    SUB(p, Register.E, rightReg)
    ADD(p, destReg, Register.D)
    LABEL3 = p.getCounter()
    SHR(p, rightReg)
    SHR(p, Register.D)
    fJZERO4 = FutureJZERO(p, Register.D)
    LABEL_JZERO4 = p.getCounter()
    fJUMP3 = FutureJUMP(p)
    LABEL_JUMP3 = p.getCounter()
    RESET(p, destReg)
    LABEL4 = p.getCounter()

    # przeniesienie reszty z dzielenia do destReg
    copy(p, destReg, Register.E)
    LABEL5 = p.getCounter()

    # wykonanie jumpów
    fJZERO_NOT_ZERO.materialize(LABEL_JZERO_ZERO - LABEL_JUMP_NOT_ZERO + 1)
    fJZERO_ZERO.materialize(LABEL5 - LABEL_JZERO_ZERO + 1)
    fJZERO.materialize(LABEL_JUMP3 - LABEL_JZERO + 1)
    fJZERO2.materialize(LABEL_JUMP - LABEL_JZERO2 + 1)
    fJUMP.materialize(LABEL0 - LABEL_JUMP + 1)
    fJZERO3.materialize(LABEL_JUMP2 - LABEL_JZERO3 + 1)
    fJUMP2.materialize(LABEL3 - LABEL_JUMP2 + 1)
    fJZERO4.materialize(LABEL4 - LABEL_JZERO4 + 1)
    fJUMP3.materialize(LABEL2 - LABEL_JUMP3 + 1)
    # reszta z dzielenia w Register.B


def CONDITION_LOWERTHAN(p, leftVal, rightVal):
    leftVal.evalueToRegisterInstruction(p, Register.B)       
    rightVal.evalueToRegisterInstruction(p, Register.C) 
    INC(p, Register.B)
    SUB(p, Register.B, Register.C)
    # Register.B = 0 -> leftVal < rightVal


def CONDITION_LOWEREQU(p, leftVal, rightVal):
    leftVal.evalueToRegisterInstruction(p, Register.B)
    rightVal.evalueToRegisterInstruction(p, Register.C)
    SUB(p, Register.B, Register.C)
    # Register.B = 0 -> leftVal <= rightVal


def CONDITION_GREATERTHAN(p, leftVal, rightVal):
    CONDITION_LOWERTHAN(p, rightVal, leftVal)
    # Register.B = 0 -> leftVal > rightVal


def CONDITION_GREATEREQU(p, leftVal, rightVal):
    CONDITION_LOWEREQU(p, rightVal, leftVal)
    # Register.B = 0 -> leftVal >= rightVal


def CONDITION_EQU(p, leftVal, rightVal):
    leftVal.evalueToRegisterInstruction(p, Register.B)
    rightVal.evalueToRegisterInstruction(p, Register.C)
    copy(p, Register.D, Register.B)
    SUB(p, Register.B, Register.C)
    SUB(p, Register.C, Register.D)
    ADD(p, Register.B, Register.C)
    # Register.B = 0 -> leftVal = rightVal


def CONDITION_INEQU(p, leftVal, rightVal):
    CONDITION_EQU(p, leftVal, rightVal)
    fJUMP_IF_EQUAL = FutureJZERO(p, Register.B)
    LABEL_JUMP_IF_EQUAL = p.getCounter()
    RESET(p, Register.B)
    fJUMP_SKIP = FutureJUMP(p)

    LABEL_EQUAL = p.getCounter()
    INC(p, Register.B)
    LABEL_NOT_EQUAL = p.getCounter()

    # wykonanie jumpów
    fJUMP_IF_EQUAL.materialize(LABEL_EQUAL - LABEL_JUMP_IF_EQUAL + 1)
    fJUMP_SKIP.materialize(LABEL_NOT_EQUAL - LABEL_EQUAL + 1)
    # Register.B = 0 -> leftVal =/= rightVal


def IF_THEN_ELSE(p, cond, thenCommands, elseCommands):
    cond.generateCode(p)

    # w Register.B znajduje się wynik instrukcji warunkowej, jeżeli Register.B = 0 (true) skocz do if
    FJZERO = FutureJZERO(p, Register.B)
    LABEL_FJZERO = p.getCounter()

    # else
    for com in elseCommands:
        com.generateCode(p)
    FJUMP = FutureJUMP(p)

    # if
    THEN_BLOCK_START_LABEL = p.getCounter()
    for com in thenCommands:
        com.generateCode(p)
    THEN_BLOCK_END_LABEL = p.getCounter()

    # wykonanie jumpów
    FJZERO.materialize(THEN_BLOCK_START_LABEL - LABEL_FJZERO + 1)
    FJUMP.materialize(THEN_BLOCK_END_LABEL - THEN_BLOCK_START_LABEL + 1)


def IF_THEN(p, cond, thenCommands):
    cond.generateCode(p)

    # w Register.B znajduje się wynik instrukcji warunkowej, jeżeli Register.B = 0 (true) skocz do if, w przeciwnym przypadku skocz na koniec
    FJZERO = FutureJZERO(p, Register.B)
    LABEL_FJZERO = p.getCounter()
    FJUMP = FutureJUMP(p)
    LABEL_FJUMP = p.getCounter()

    # if
    THEN_BLOCK_START_LABEL = p.getCounter()
    for com in thenCommands:
        com.generateCode(p)
    THEN_BLOCK_END_LABEL = p.getCounter()

    # wykonanie jumpów
    FJZERO.materialize(THEN_BLOCK_START_LABEL - LABEL_FJZERO + 1)
    FJUMP.materialize(THEN_BLOCK_END_LABEL - LABEL_FJUMP + 1)


def WHILE(p, cond, commands):
    LABEL_WHILE_CONDITION = p.getCounter()
    cond.generateCode(p)

    # w Register.B znajduje się wynik instrukcji warunkowej, jeżeli Register.B = 0 (true) skocz do while
    fJUMP_INTO_WHILE = FutureJZERO(p, Register.B)
    LABEL_FJUMPINTOWHILE = p.getCounter()

    # Register.B != 0 (false), wyjdź z while, skocz na koniec
    fJUMP_OUT_WHILE = FutureJUMP(p)

    # instrukcje w while
    LABEL_WHILE_INSIDE = p.getCounter()
    for com in commands:
        com.generateCode(p)
    fJUMP_LOOP = FutureJUMP(p)
    LABEL_WHILE_END = p.getCounter()

    # wykonanie jumpów
    fJUMP_INTO_WHILE.materialize(LABEL_WHILE_INSIDE - LABEL_FJUMPINTOWHILE + 1)
    fJUMP_OUT_WHILE.materialize(LABEL_WHILE_END - LABEL_WHILE_INSIDE + 1)
    fJUMP_LOOP.materialize(LABEL_WHILE_CONDITION - LABEL_WHILE_END + 1)


def REPEAT_UNTIL(p, cond, commands):
    LABEL_REPEAT_INSIDE = p.getCounter()

    # wykonaj instrukcje w repeat
    for com in commands:
        com.generateCode(p)
    cond.generateCode(p)

    # w Register.B znajduje się wynik instrukcji warunkowej, jeżeli Register.B = 0 (true) skocz na koniec, zakończ pętlę
    fJUMP_END = FutureJZERO(p, Register.B)
    LABEL_JUMP_END = p.getCounter()

    # Register.B != 0 (false), wykonaj pętlę, skocz do repeat
    fJUMP_INTO_REPEAT = FutureJUMP(p)
    LABEL_FJUMPINTOREPEAT = p.getCounter()

    # wykonanie jumpów
    fJUMP_END.materialize(LABEL_FJUMPINTOREPEAT - LABEL_JUMP_END + 1)
    fJUMP_INTO_REPEAT.materialize(LABEL_REPEAT_INSIDE - LABEL_FJUMPINTOREPEAT + 1)


def FOR_TO(p, rangeFromValue, rangeToValue, identifier, commands):
    # rangeFrom
    rangeFromValue.evalueToRegisterInstruction(p, Register.B)
    identifier.memoryAddressToRegister(p, Register.A, None)
    Memory.initialize(identifier.pidentifier)
    STORE(p, Register.B, Register.A)

    # kopia rangeTo
    rangeToValue.evalueToRegisterInstruction(p, Register.F)
    rangeToValueMemBlockCopy = Memory.getUnnamedMemoryBlock()
    setRegisterConst(p, Register.A, rangeToValueMemBlockCopy)
    STORE(p, Register.F, Register.A)

    # licznik pętli, idzie od n w dół
    INC(p, Register.F)
    SUB(p, Register.F, Register.B)

    LABEL_LOOP = p.getCounter()

    # jeżeli Register.F = 0 zakończ pętlę, skocz na koniec
    fJUMP_TO_END_IF_ITERATOR_IS_ZERO = FutureJZERO(p, Register.F)
    LABEL_JUMP_TO_END_IF_ITERATOR_IS_ZERO = p.getCounter()

    for com in commands:
        com.generateCode(p)
        if isinstance(com, CommandForTo):
            identifier.memoryAddressToRegister(p, Register.A, None)
            LOAD(p, Register.B, Register.A)

            setRegisterConst(p, Register.A, rangeToValueMemBlockCopy)
            LOAD(p, Register.F, Register.A)

            INC(p, Register.F)
            SUB(p, Register.F, Register.B)

    DEC(p, Register.F)

    setRegisterConst(p, Register.A, rangeToValueMemBlockCopy)
    LOAD(p, Register.B, Register.A)

    INC(p, Register.B)
    identifier.memoryAddressToRegister(p, Register.A, None)
    SUB(p, Register.B, Register.F)
    Memory.initialize(identifier.pidentifier)
    STORE(p, Register.B, Register.A)

    fJUMP_LOOP = FutureJUMP(p)
    LABEL_END_FOR = p.getCounter()

    # wykonanie jumpów
    fJUMP_TO_END_IF_ITERATOR_IS_ZERO.materialize(LABEL_END_FOR - LABEL_JUMP_TO_END_IF_ITERATOR_IS_ZERO + 1)
    fJUMP_LOOP.materialize(LABEL_LOOP - LABEL_END_FOR + 1)


def FOR_DOWNTO(p, rangeFromValue, rangeToValue, identifier, commands):
    # kopia rangeTo
    rangeToValue.evalueToRegisterInstruction(p, Register.B)
    rangeToValueMemBlockCopy = Memory.getUnnamedMemoryBlock()
    setRegisterConst(p, Register.A, rangeToValueMemBlockCopy)
    STORE(p, Register.B, Register.A)

    # kopia rangeFrom
    rangeFromValue.evalueToRegisterInstruction(p, Register.F)
    identifier.memoryAddressToRegister(p, Register.A, None)
    Memory.initialize(identifier.pidentifier)
    STORE(p, Register.F, Register.A)

    # licznik pętli
    INC(p, Register.F)
    SUB(p, Register.F, Register.B)

    LABEL_LOOP = p.getCounter()

    # jeżeli Register.F = 0 zakończ pętlę, skocz na koniec
    fJUMP_TO_END_IF_ITERATOR_IS_ZERO = FutureJZERO(p, Register.F)
    LABEL_JUMP_TO_END_IF_ITERATOR_IS_ZERO = p.getCounter()

    for com in commands:
        com.generateCode(p)
        if isinstance(com, CommandForTo):
            identifier.memoryAddressToRegister(p, Register.A, None)
            LOAD(p, Register.F, Register.A)
            INC(p, Register.F)

            setRegisterConst(p, Register.A, rangeToValueMemBlockCopy)
            LOAD(p, Register.B, Register.A)

            SUB(p, Register.F, Register.B)

    DEC(p, Register.F)

    setRegisterConst(p, Register.A, rangeToValueMemBlockCopy)
    LOAD(p, Register.B, Register.A)

    identifier.memoryAddressToRegister(p, Register.A, None)
    ADD(p, Register.B, Register.F)
    # iterator down to
    DEC(p, Register.B)
    Memory.initialize(identifier.pidentifier)
    STORE(p, Register.B, Register.A)

    fJUMP_LOOP = FutureJUMP(p)
    LABEL_END_FOR = p.getCounter()

    # wykonanie jumpów
    fJUMP_TO_END_IF_ITERATOR_IS_ZERO.materialize(LABEL_END_FOR - LABEL_JUMP_TO_END_IF_ITERATOR_IS_ZERO + 1)
    fJUMP_LOOP.materialize(LABEL_LOOP - LABEL_END_FOR + 1)