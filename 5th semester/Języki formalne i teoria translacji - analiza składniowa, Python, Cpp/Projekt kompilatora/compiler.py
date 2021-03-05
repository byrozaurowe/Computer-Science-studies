# Wiktoria Byra 250131, Języki formalne i teoria translacji, projekt kompilatora, 2021

from parser import parser, lexer
import sys

def readFromFile(fname):
    with open(fname, "r") as file:
        return file.read()


def writeToFile(fname, data):
    with open(fname, "w") as file:
        file.write(data)


inputFile = sys.argv[1]
outFile = sys.argv[2]

try:
    data = readFromFile(inputFile)
    program = parser.parse(data)
    output = program.generateCode()
    writeToFile(outFile, output)
except Exception as err:
    print(err)
    exit(1)