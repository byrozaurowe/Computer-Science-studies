# Wiktoria Byra, zadanie 7 lista 1 laboratorium Obliczenia naukowe

# funkcja, którą będziemy pochodniować
function func(x)
    return sin(x) + cos(3 * x)
end
# dokładna pochodna funkcji
function df(x)
    return cos(x) - 3 * sin(3 * x)
end
# główna funkcja obliczająca przybliżenie pochodnej i błąd przybliżenia
function derivative(x)
    df_approximation::Float64 = 0.0 # tutaj będzie zapisane przybliżenie pochodnej
    df_exact::Float64 = df(x) # dokładna wartość pochodnej
    error::Float64 = 0.0 # tutaj będzie zapisany błąd przybliżenia
    two::Float64 = 2.0
    for i = 0:54
        h::Float64 = two ^ (-1 * i) # przyrost zmiennej niezależnej x
        df_approximation = (func(x + h) - func(x)) / h
        error = abs(df_exact - df_approximation)
        println("dla h = ", h)
        println("przybliżenie pochodnej = ", df_approximation)
        println("błąd = ", error, "\n")
    end
end
# main wywołujący docelowa funkcję
function main()
    x::Float64 = 1
    derivative(x)
end