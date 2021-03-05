# Wiktoria Byra 250131, Języki formalne i teoria translacji, projekt kompilatora, 2021

from enum import Enum

class Register(Enum):
    A = 'a'
    B = 'b'
    C = 'c'
    D = 'd'
    E = 'e'
    F = 'f'

    def __str__(self):
        return self.value