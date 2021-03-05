# Wiktoria Byra 250131, Języki formalne i teoria translacji, projekt kompilatora, 2021

import instructions

class Condition:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def generateCode(self, p):
        if self.operator == '>':
            return instructions.CONDITION_GREATERTHAN(p, self.left, self.right)
        if self.operator == '>=':
            return instructions.CONDITION_GREATEREQU(p, self.left, self.right)
        if self.operator == '<':
            return instructions.CONDITION_LOWERTHAN(p, self.left, self.right)
        if self.operator == '<=':
            return instructions.CONDITION_LOWEREQU(p, self.left, self.right)
        if self.operator == '=':
            return instructions.CONDITION_EQU(p, self.left, self.right)
        if self.operator == '!=':
            return instructions.CONDITION_INEQU(p, self.left, self.right)
        else:
            raise Exception("Niezdefiniowany operator '%s'" % self.operator)