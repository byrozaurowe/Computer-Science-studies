# Wiktoria Byra 250131, Języki formalne i teoria translacji, projekt kompilatora, 2021

from memory import manager as Memory
import instructions

class Identifier:
    def __init__(self, pidentifier):
        self.pidentifier = pidentifier

    @property
    def declaration(self):
        return Memory.getDeclarationByPidentifier(self.pidentifier)

    def memoryAddressToRegister(self, p, reg1, reg2):
        memoryId = Memory.getBlockId(self.pidentifier)
        instructions.setRegisterConst(p, reg1, memoryId)

class ArrayAccess(Identifier):
    def __init__(self, pidentifier, index):
        super(ArrayAccess, self).__init__(pidentifier)
        self.index = index

    def evalueArrayOffsetToRegister(self, p, reg):
        raise Exception("Funkcja nie zdefiniowana")

    def memoryAddressToRegister(self, p, reg1, reg2):
        raise Exception("Funkcja nie zdefiniowana")

class ArrayAccessByNum(ArrayAccess):
    def __init__(self, pidentifier, num):
        super(ArrayAccessByNum, self).__init__(pidentifier, num)

    def memoryAddressToRegister(self, p, reg1, reg2):
        declaration = self.declaration

        if not declaration.isArray():
            raise Exception("'%s' nie jest tablicą" % declaration.pidentifier)

        memoryId = Memory.getBlockId(self.pidentifier)
        arrRangeFrom = declaration.rangeFrom
        arrRangeTo = declaration.rangeTo
        offset = self.index - arrRangeFrom
        if offset < 0 :
            raise Exception("Przekorczenie zkresu tablicy, podano %i, a zakres wynosi (%i:%i)" % (self.index, arrRangeFrom, arrRangeTo))
        instructions.setRegisterConst(p, reg2, offset)
        instructions.setRegisterConst(p, reg1, memoryId)
        instructions.ADD(p, reg1, reg2)

class ArrayAccessByPidentifier(ArrayAccess):
    def __init__(self, pidentifier, pid):
        super(ArrayAccessByPidentifier, self).__init__(pidentifier, pid)

    def memoryAddressToRegister(self, p, reg1, reg2):
        declaration = self.declaration

        if not declaration.isArray():
            raise Exception("'%s' nie jest tablicą" % declaration.pidentifier)

        memoryId = declaration.memoryId
        arrRangeFrom = declaration.rangeFrom
        arrRangeTo = declaration.rangeTo
    
        indexIdentifier = Identifier(self.index)
        if Memory.isInitialized(indexIdentifier.pidentifier) == False:
            raise Exception("Użycie niezainicjalizowanej zmiennej %s" % indexIdentifier.pidentifier)

        instructions.LOAD_IDENTIFIER_VALUE_TO_REGISTER(p, indexIdentifier, reg2)
        instructions.setRegisterConst(p, reg1, arrRangeFrom)
        instructions.SUB(p, reg2, reg1)
        instructions.setRegisterConst(p, reg1, memoryId)
        instructions.ADD(p, reg1, reg2)
