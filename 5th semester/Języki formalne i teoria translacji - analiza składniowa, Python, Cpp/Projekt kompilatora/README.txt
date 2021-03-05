Wiktoria Byra, nr indeksu: 250131
Języki formalne i teoria translacji, prowadzący: prof. Maciej Gębala

Sposób uruchomienia:
> python3 compiler.py input out
gdzie "input" to ścieżka pliku wejściowego, a "output" to plik wyjściowy, w którym zostanie zapisany wygenerowany kod maszynowy.

Instalacja wymaganych plików:
sudo apt update
sudo apt install python3
sudo apt install python3-pip
pip3 install ply

Krótki opis plikow:
compiler.py - główny program, czytający dane z pliku, wywołujący parser, generowanie kodu maszynowego i zapisujący dane do pliku
tokenizer.py - analiza leksykalna
parser.py - parser
program.py - klasa przetrzymująca deklaracje, komendy, instrukcje i zliczająca linijki kodu
register.py - klasa rejestrów
memory.py - obsługa komórek pamięci
instructions.py - definicje instrukcji języka maszynowego
declaration.py - deklaracja nowych zmiennych i tablic
identifier.py - dostęp do zmiennych i tablic
condition.py - wyrażenia warunkowe
expression.py - wyrażenia arytmetyczne
command.py - komendy if, read, write, pętle for, while i repeat

Program przetestowany na Ubuntu 18.04.4 z Python 3.6.9 i PLY 3.11.