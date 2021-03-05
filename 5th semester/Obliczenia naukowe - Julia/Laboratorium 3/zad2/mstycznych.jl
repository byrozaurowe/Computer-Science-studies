# autor: Wiktoria Byra, zadanie 2 lista 3 Obliczenia naukowe

function mstycznych(f, pf, x0::Float64, delta::Float64, epsilon::Float64, maxit::Int)
    #= f, pf – funkcją f(x) oraz pochodną f'(x) zadane jako anonimowe funkcje,
     x0 – przybliżenie początkowe,
     delta,epsilon – dokładności obliczeń, 
     maxit – maksymalna dopuszczalna liczba iteracji, =#
    v = f(x0)
    if (abs(v) < epsilon)
        r = x0
        it = 0
        err = 2
        return (r, v, it, err)
        #= r – przybliżenie pierwiastka równania f(x) = 0,
        v – wartość f(r),
        it – liczba wykonanych iteracji,
        err – sygnalizacja błędu
            0 - metoda zbieżna
            1 - nie osiągnięto wymaganej dokładności w maxit iteracji,
            2 - pochodna bliska zeru =#
    end 
    for it = 1:maxit
        r = x0 - v/pf(x0)
        v = f(r)
        if (abs(r - x0) < delta || abs(v) < epsilon)
            err = 0
            return (r, v, it, err)
        end 
        x0 = r
        end
    r = NaN
    v = NaN
    it = NaN
    err = 1
    return (r, v, it, err)
end
