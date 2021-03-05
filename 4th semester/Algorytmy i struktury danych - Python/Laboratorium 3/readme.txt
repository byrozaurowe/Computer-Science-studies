Zad. 1
sposób użycia:
python3 aisd1.py --type radix --comp ">="|"<="
wpisujemy n
wprowadzamy n liczb do posortowania

program zwraca tablicę posortowaną za pomocą algorytmu radix sort

LUB python3 aisd1.py --type radix quick|merge|dual-pivot|insert --comp ">="|"<=" --stat nazwa_pliku1 nazwa_pliku2 k
na wejściu należy wybrać z jakim rodzajem sortowania chcemy porównać radix sorta, podać monotoniczność oraz nazwy plików, do których mają zostać zapisane statystyki

program wyświetla wykres porównujący czas działania radix sorta z danym sortem

Radix sort wypada korzystnie pod względem czasu wykonania przy dużych rozmiarach tablic i przy dużym zakresie losowanych liczb (>= 2n). Radix sort nie bazuje na porównaniach i przestawieniach, więc nie można obliczyć ich liczby i porównać radixa z innymi metodami pod tym względem.

Zad. 2 
Program aisd2.py działa zgodnie z wymaganiami na liście - przymuje parametr wejściowy "-r|-p" oraz dane n i k, pokazuje działaniealgorytmów i zwraca tablicę z zaznaczonym szukanym elementem.

Program aisd2_1.py służy do testów statystycznych - wykonuje 10000 razy select i random select dla danej wielkości tablicy n i zwraca minimalną, maksymalną oraz średnią liczbę porównań, a także oblicza odchylenie standadowe.
Random select średnio wykonuje mniej porównań od zwykłego selecta. Wynika to z tego, że przy dobrym doborze danych losowych może wykonać program nawet w czasie 1*n. Natomiast maksymalna liczba porównań w random select bywa dużo większa, czyli w niektórych przypadkach wykonania jest on nawet dwukrotnie wolniejszy od zwykłego selecta.

Zad. 4
sposób użycia:
python3 aisd4.py --type select-quick quick --comp ">="|"<=" --stat nazwapliku1 nazwapliku2

Program pokazuje porównanie statystyk działania quick sorta i quick sorta z wykorzystaniem algorytmu select do wyznaczenia mediany (na pivot). Jak widać select nie przyspieszył działania quick sorta, statystyki wypadają porównywalnie (wykres w pliku wykres.png).  Prawdopodnie wynika to z tego, że dane są losowe i rzadko pojawia się najgorszy przypadek, na którym nasz select ulepszyłby program.
