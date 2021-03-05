# Wiktoria Byra, zadanie 4 lista 1 laboratorium Obliczenia naukowe

#funkcja znajdująca najmniejszą liczbę x z przedziału 1-2, taką że x*(1/x)!=1
function find() 
    # zaczynamy od najmniejszej liczby >1
    start::Float64 = nextfloat(Float64(1.0))
    one::Float64 = 1.0
    # sprawdzamy czy liczba spełnia warunek, jeżeli tak to kończymy działanie pętli, w przeciwnym przypadku zwiększamy liczbę o macheps i kontunuujemy
    while start < 2.0
        result = start * (one / start)
        if result != one
            println("result = ", result)
            println("x = ", start)
            break
        end
        start = nextfloat(Float64(start))
    end
end