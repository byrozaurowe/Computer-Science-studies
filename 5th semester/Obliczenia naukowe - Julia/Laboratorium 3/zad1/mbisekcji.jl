# autor: Wiktoria Byra, zadanie 1 lista 3 Obliczenia naukowe

function mbisekcji(f, a::Float64, b::Float64,
    delta::Float64, epsilon::Float64)
    #= f – funkcja f(x) zadana jako anonimowa funkcja (ang. anonymous function),
     a,b – końce przedziału początkowego,
     delta,epsilon – dokładności obliczeń, =#
    M = 1000
    u = f(a)
    v = f(b)
    e = b - a
    if (sign(u) == sign(v))
        err = 1
        r = NaN
        v = NaN
        it = NaN
        return (r, v, it, err)
        #= r – przybliżenie pierwiastka równania f(x) = 0,
        v – wartość f(r),
        it – liczba wykonanych iteracji,
        err – sygnalizacja błędu
            0 - brak błędu
            1 - funkcja nie zmienia znaku w przedziale [a,b] =#
    end 
    for it = 1:M
        e = e/2
        r = a + e
        v = f(r)
        if (abs(e) < delta || abs(v) < epsilon)
            err = 0
            return (r, v, it, err)
        end 
        if (sign(v) != sign(u))
            b = r
            v = v
        else
            a = r
            u = v
        end 
    end
end
