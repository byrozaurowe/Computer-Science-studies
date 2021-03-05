Zad. 1
python3 aisd1.py --type quick|merge|insert --cmp '>='|'<=' 
LUB python3 aisd1.py --cmp '>='|'<=' --type quick|merge|insert 
wpisujemy n
następnie n liczb do sortowania.

przykład użycia:
python3 aisd1.py --type insert --comp ">="
5
1
10
111
1
3

wynik:
Czas działania algorytmu: 5.936622619628906e-05
Liczba porównań: 7
[111, 10, 3, 1, 1]

Zad. 2
python3 aisd2.py --type quick|merge|insert|dual-pivot --cmp '>='|'<=' --stat nazwa_pliku k
LUB python3 aisd2.py --cmp '>='|'<=' --type quick|merge|insert|dual-pivot --stat nazwa_pliku k

statystyki zapisują się w pliku nazwa_pliku.txt a wykresy wyświetlają się na ekranie


Zad. 3
python3 aisd3.py --type quick|merge|insert|dual-pivot quick|merge|insert|dual-pivot --cmp '>='|'<=' --stat nazwa_pliku1 nazwa_pliku2 k
LUB python3 aisd2.py --cmp '>='|'<=' --type quick|merge|insert|dual-pivot quick|merge|insert|dual-pivot --stat nazwa_pliku1 nazwa_pliku2 k

na wejściu podajemy dwa typy sortowań, które chcemy porównać i dwie nazwy plików, do których zapiszą się statystyki poszczególnych sortowań

przykład użycia:
python3 aisd3.py --type dual-pivot quick --comp "<=" --stat statDual statQuick 10

wykres porównujący dual-pivot sorta i quick sorta w pliku wykres.png

Algorytm dual-pivot sort wykonuje więcej porównań i działa w dłuższym czasie niż quick sort, ale za to wykonuje mniej przestawień. Z wzrotem rozmiaru tablicy różnice są coraz bardziej widoczne.
 
Eksperymentalne wyznaczanie stałej(średnia ilość porównań w dual pivot sort)/(średnia ilość porównań w quick sort): dla róźnych n wyznaczałam liczbę porównań kluczy w dual-pivot sorcie i quick sorcie, iloraz zawsze oscylował w okolicach n = 1.7

Zad. 4 python3 aisd4.py --type hybrid quick|merge|insert|dual-pivot --cmp '>='|'<=' --stat nazwa_pliku1 nazwa_pliku2 k

przykład użycia:
python3 aisd4.py --type hybrid quick --comp "<=" --stat statHybrid statQuick 10

na wejściu podajemy z jakim typem sortowania chcemy porównać algorytm hybrydowy

wykres porównujący hybrid sorta i quick sorta w plik wykres2.png

Algorytm hybrydowy korzysta z metory quick sort, dopóki tablica ma więcej niż 10 elementów. Przy 10 elementach przechodiz na insertion sort. Algorytm hybrydowy wykonuje minimalnie mnije porównań i jest szybszy niż quick sort.

