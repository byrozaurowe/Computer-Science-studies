# Wiktoria Byra 250131, Języki formalne i teoria translacji, projekt kompilatora, 2021

from memory import manager as Memory

class VariableDeclaration:
    def __init__(self, pidentifier, isarr = False, islocal = False, lineNumber = -1):
        self.lineNumber = lineNumber
        self.memoryId = None
        self.pidentifier = pidentifier
        self.isarr = isarr
        self.length = 1
        self.islocal = islocal
        self.initialized = False

    def register(self):
        self.initialized = True
        Memory.assignMemory(self)

    def delete(self):
        Memory.unregister(self)

    def isArray(self):
        return self.isarr == True

    def __repr__(self):
        return str((self.pidentifier, self.memoryId, self.length, "Array" if self.isarr else "Var"))

class ArrayDeclaration(VariableDeclaration):
    def __init__(self, pidentifier, rangeFrom, rangeTo, line):
        super(ArrayDeclaration, self).__init__(pidentifier, True, lineNumber=line)
        if rangeFrom > rangeTo:
            raise Exception("Nieprawidłowy zakres tablicy %s(%i:%i) w linii %i" % (pidentifier, rangeFrom, rangeTo, line))
        self.rangeFrom = rangeFrom
        self.rangeTo = rangeTo
        self.length = rangeTo - rangeFrom + 1