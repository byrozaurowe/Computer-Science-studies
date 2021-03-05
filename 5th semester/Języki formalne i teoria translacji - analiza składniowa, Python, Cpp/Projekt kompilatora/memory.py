# Wiktoria Byra 250131, Języki formalne i teoria translacji, projekt kompilatora, 2021

class MemoryException(Exception):
    pass


class Memory:
    def __init__(self):
        self.declarations = None
        self.declaredPidentifiers = set()
        self.memmap = {}
        self.initialized = {}
        self.lastblockid = 0

    def runMemoryCheck(self, declarations):
        self.declarations = declarations
        self.checkDuplicateDeclarations()

    def checkDuplicateDeclarations(self):
        for decl in self.declarations:
            pidentifier = decl.pidentifier
            if pidentifier in self.declaredPidentifiers:
                raise Exception("Zduplikowana deklaracja zmiennej '%s' w linii %i" % (pidentifier, decl.lineNumber))
            self.declaredPidentifiers.add(pidentifier)

    def unregister(self, declaration):
        try:
            del self.memmap[declaration.pidentifier]
            declaration.memoryId = None
        except KeyError as key:
            raise Exception("Nie ma takiej zarejestrowanej zmiennej %s" % key)

    def assignMemory(self, declaration):
        pidentifier = declaration.pidentifier

        if pidentifier in self.memmap and self.memmap[pidentifier].memoryId != None:
            raise Exception("Duplikacja alokacji pamięci")

        blockLength = 1
        if declaration.isArray():
            blockLength = declaration.length

        assignedMemoryBlockId = self.lastblockid
        
        self.memmap[pidentifier] = declaration
        declaration.memoryId = assignedMemoryBlockId

        self.lastblockid += blockLength

    def assignMemoryToDeclarations(self):
        for declaration in self.declarations:
            self.assignMemory(declaration)

    def getUnnamedMemoryBlock(self):
        assignedMem = self.lastblockid
        self.lastblockid += 1
        return assignedMem
        
    def getSymbols(self):
        return self.memmap.keys()

    def initialize(self, pid):
        if not pid in self.initialized:
            self.initialized[pid] = True

    def isInitialized(self, pid):
        if not pid in self.initialized:
            return False
        else:
            return True

    def getBlockId(self, name):
        try:
            memoryId = self.memmap[name].memoryId
            if memoryId == None:
                raise Exception("'%s' nie ma zaalokowanej pamięci" % name)
            return memoryId
        except KeyError:
            raise Exception("Niezadeklarowana zmienna '%s'" % name)

    def getDeclarationByPidentifier(self, pid):
        if pid not in self.memmap:
            raise Exception("Niezadeklarowana zmienna '%s'" % pid)

        decl = self.memmap[pid]
        if not decl:
            raise Exception("Niezadeklarowana zmienna '%s'" % pid)
        return decl

manager = Memory()
