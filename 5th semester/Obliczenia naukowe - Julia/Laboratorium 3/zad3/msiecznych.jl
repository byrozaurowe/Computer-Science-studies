# autor: Wiktoria Byra, zadanie 3 lista 3 Obliczenia naukowe

function msiecznych(f, x0::Float64, x1::Float64, delta::Float64, epsilon::Float64, maxit::Int)
    #= f – funkcją f(x) zadana jako anonimowa funkcja,
     x0, x1 – przybliżenia początkowe,
     delta,epsilon – dokładności obliczeń, 
     maxit – maksymalna dopuszczalna liczba iteracji, =#
    fa = f(x0)
    fb = f(x1)
    for it = 1:maxit
        if (abs(fa) > abs(fb))
            x0,x1 = x1,x0
            fa,fb = fb,fa
        end
        s = (x1 - x0)/(fb - fa)
        x1 = x0
        fb = fa
        x0 = x0 - fa*s
        fa = f(x0)
        if (abs(x1-x0) < delta || abs(fa) < epsilon)
            r = x0
            v = fa
            err = 0
            return (r, v, it, err)
            #= r – przybliżenie pierwiastka równania f(x) = 0,
            v – wartość f(r),
            it – liczba wykonanych iteracji,
            err – sygnalizacja błędu
                0 - metoda zbieżna
                1 - nie osiągnięto wymaganej dokładności w maxit iteracji, =#
        end
    end 
    r = NaN
    v = NaN
    it = NaN
    err = 1
    return (r, v, it, err)
end