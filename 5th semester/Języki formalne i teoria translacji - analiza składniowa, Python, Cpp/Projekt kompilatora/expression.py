# Wiktoria Byra 250131, Języki formalne i teoria translacji, projekt kompilatora, 2021

import instructions
from identifier import ArrayAccess

class Expression:
    def evalueToRegisterInstruction(self, p, reg):
        raise Exception("Funkcja evalueToRegisterInstruction() niezdefiniowana dla %s" % self.__class__)

    def memoryAddressToRegisterInstruction(self, p, reg):
        raise Exception("Funkcja memoryAddressToRegisterInstruction() niezdefiniowana dla %s" % self.__class__)


class Number(Expression):
    def __init__(self, num):
        self.num = num

    def evalueToRegisterInstruction(self, p, reg):
        return instructions.LOAD_NUMBER_VALUE_TO_REGISTER(p, self.num, reg)

    def memoryAddressToRegisterInstruction(self, p, reg):
        return instructions.LOAD_NUMBER_MEMADDR_TO_REGISTER(p, self.num, reg)


class ValueFromIdentifier(Expression):
    def __init__(self, identifier, lineNumber=-1):
        self.identifier = identifier
        self.lineNumber = lineNumber

    def evalueToRegisterInstruction(self, p, reg):
        try:
            isInitialized = self.identifier.declaration.initialized
            if isInitialized == False:
                raise Exception("Użycie niezainicjalizowanej zmiennej '%s' " % self.identifier.pidentifier)
            if isinstance(self.identifier, ArrayAccess):
                return instructions.LOAD_ARRAY_VALUE_TO_REGISTER(p, self.identifier, reg)
            return instructions.LOAD_IDENTIFIER_VALUE_TO_REGISTER(p, self.identifier, reg)
        except Exception as err:
            raise Exception(str(err))
        
    def memoryAddressToRegisterInstruction(self, p, reg):
        try:
            isInitialized = self.identifier.declaration.initialized
            if isInitialized == False:
                raise Exception("Użycie niezainicjalizowanej zmiennej '%s' " % self.identifier.pidentifier)
            if isinstance(self.identifier, ArrayAccess):
                return instructions.LOAD_ARRAY_MEMADDR_TO_REGISTER(p, self.identifier, reg)
            return instructions.LOAD_IDENTIFIER_MEMADDR_TO_REGISTER(p, self.identifier, reg)
        except Exception as err:
            raise Exception(str(err))

class Operator(Expression):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def evalueToRegisterInstruction(self, p, reg):
        if self.operator == '+':
            return instructions.PLUS(p, self.left, self.right, reg)
        if self.operator == '-':
            return instructions.MINUS(p, self.left, self.right, reg)
        if self.operator == '*':
            return instructions.MULTIPLY(p, self.left, self.right, reg)
        if self.operator == '/':
            return instructions.DIVIDE(p, self.left, self.right, reg)
        if self.operator == '%':
            return instructions.MODULO(p, self.left, self.right, reg)
        else:
            raise Exception("Operator '%s' niezdefiniowany" % self.operator)

    def memAddrToToRegInstr(self, p, reg):
        if self.operator == '+':
            return instructions.PLUS(p, self.left, self.right, reg)
        if self.operator == '-':
            return instructions.MINUS(p, self.left, self.right, reg)
        if self.operator == '*':
            return instructions.MULTIPLY(p, self.left, self.right, reg)
        if self.operator == '/':
            return instructions.DIVIDE(p, self.left, self.right, reg)
        if self.operator == '%':
            return instructions.MODULO(p, self.left, self.right, reg)
        else:
            raise Exception("Operator '%s' niezdefiniowany" % self.operator)