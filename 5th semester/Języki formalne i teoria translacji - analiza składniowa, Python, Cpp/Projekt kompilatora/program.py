# Wiktoria Byra 250131, Języki formalne i teoria translacji, projekt kompilatora, 2021

from memory import manager as Memory

class Program:
    def __init__(self, commands, declarations = []):
        self.declarations = declarations
        self.commands = commands
        self.instructions = []
        self.counter = 0
        Memory.runMemoryCheck(self.declarations)
        Memory.assignMemoryToDeclarations()
        self.processCommands()

    def getCounter(self):
        return self.counter

    def incrementCounter(self):
        self.counter += 1
        return self

    def addFutureInstruction(self, future):
        self.incrementCounter()
        self.instructions.append(future)
        return self.counter - 1

    def makeInstruction(self, instr, X, Y=""):
        instrStr = "%s %s %s" % (instr, X, Y)
        self.incrementCounter()
        self.instructions.append(instrStr)

    def processCommands(self):
        for com in self.commands:
            com.generateCode(self)

    def generateCode(self):
        return '\n'.join(self.instructions + ["HALT"])