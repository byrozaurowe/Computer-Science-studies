# Wiktoria Byra 250131, Języki formalne i teoria translacji, projekt kompilatora, 2021

import instructions
from declaration import VariableDeclaration
from identifier import Identifier
from expression import ValueFromIdentifier
from memory import manager as Memory


class Command:
    def __init__(self, lineNumber = -1):
        self.lineNumber = lineNumber

    def generateCode(self, program):
        raise Exception("Funkcja generateCode() nie zdefiniowana dla %s" % self.__class__)


class CommandRead(Command):
    def __init__(self, identifier):
        super(CommandRead, self).__init__()
        self.identifier = identifier

    def generateCode(self, p):
        self.identifier.declaration.initialized = True
        instructions.READ(p, self.identifier)


class CommandWrite(Command):
    def __init__(self, value):
        super(CommandWrite, self).__init__()
        self.value = value

    def generateCode(self, p):
        instructions.WRITE(p, self.value)


class CommandAssign(Command):
    def __init__(self, identifier, expression, line=-1):
        super(CommandAssign, self).__init__(lineNumber=line)
        self.identifier = identifier
        self.expression = expression

    def generateCode(self, p):
        self.identifier.declaration.initialized = True
        try:
            return instructions.ASSIGN(p, self.identifier, self.expression)
        except Exception as err:
            raise Exception(str(err) + " w linii %i" % self.lineNumber)


class CommandIfThen(Command):
    def __init__(self, condition, thenCommands):
        super(CommandIfThen, self).__init__()
        self.condition = condition
        self.thenCommands = thenCommands

    def generateCode(self, p):
        instructions.IF_THEN(
            p, self.condition, self.thenCommands)


class CommandIfThenElse(CommandIfThen):
    def __init__(self, condition, thenCommands, elseCommands):
        super(CommandIfThenElse, self).__init__(condition, thenCommands)
        self.elseCommands = elseCommands

    def generateCode(self, p):
        instructions.IF_THEN_ELSE(
            p, self.condition, self.thenCommands, self.elseCommands)


class CommandWhile(Command):
    def __init__(self, condition, commands):
        super(CommandWhile, self).__init__()
        self.condition = condition
        self.commands = commands

    def generateCode(self, p):
        return instructions.WHILE(p, self.condition, self.commands)


class CommandRepeatUntil(Command):
    def __init__(self, commands, condition):
        super(CommandRepeatUntil, self).__init__()
        self.commands = commands
        self.condition = condition

    def generateCode(self, p):
        return instructions.REPEAT_UNTIL(p, self.condition, self.commands)

class CommandForTo(Command):
    def __init__(self, pidentifier, fromValue, toValue, commands, line=-1):
        super(CommandForTo, self).__init__(lineNumber=line)
        self.pidentifier = pidentifier
        self.fromValue = fromValue
        self.toValue = toValue
        self.commands = commands
        if isinstance(self.toValue, ValueFromIdentifier):
            if self.toValue.identifier.pidentifier == self.pidentifier:
                raise Exception("Użycie iteratora '%s' jako TO w pętli FOR w linii %i" % (self.pidentifier, self.lineNumber))
        if isinstance(self.fromValue, ValueFromIdentifier):
            if self.fromValue.identifier.pidentifier == self.pidentifier:
                raise Exception("Użycie iteratora '%s' jako FROM w pętli FOR w linii %i" % (self.pidentifier, self.lineNumber))

    def generateCode(self, p):
        declaredIterator = VariableDeclaration(self.pidentifier, islocal=True)
        declaredIterator.register()
        iteratorIdentifier = Identifier(self.pidentifier)
        instructions.FOR_TO(p, self.fromValue, self.toValue,
                            iteratorIdentifier, self.commands)
        declaredIterator.delete()


class CommandForDownto(CommandForTo):
    def __init__(self, pidentifier, fromValue, toValue, commands):
        super(CommandForDownto, self).__init__(
            pidentifier, fromValue, toValue, commands)

    def generateCode(self, p):
        declaredIterator = VariableDeclaration(self.pidentifier, islocal=True)
        declaredIterator.register()
        iteratorIdentifier = Identifier(self.pidentifier)
        instructions.FOR_DOWNTO(p, self.fromValue, self.toValue,
                                iteratorIdentifier, self.commands)
        declaredIterator.delete()
