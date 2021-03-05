# Wiktoria Byra, zadanie 6 lista 2 laboratorium Obliczenia naukowe

using Plots

# funkcja rekurencyjna obliczajaca wartość wielomianu
function rek(c, n, x0, X, Y)
    if n == 0
        push!(X, n)
        push!(Y, x0)
        return x0, X, Y
    else
        pom, X, Y = rek(c, n-1, x0, X, Y)
        push!(X, n)
        push!(Y, pom * pom + c)
        return pom * pom + c, X, Y
    end
end

# funkcja wywołująca funkcję wilomianową dla odpowiednich argumentów wejściowych i rysująca wykresy
function func(c, x0)
    X = []
    Y = []
    out, X, Y = rek(c, 40, x0, X, Y)
    plot(X, Y)
    println(X)
    println(Y)
    println("c = $c, x0 = $x0, f = $out")
end

function main()
    c::Float64 = -2
    x0::Float64 = 1
    func(c, x0)
    x0 = 2
    func(c, x0)
    x0 = 1.99999999999999
    func(c, x0)
    c = -1
    x0 = 1
    func(c, x0)
    x0 = -1
    func(c, x0)
    x0 = 0.75
    func(c, x0)
    x0 = 0.25
    func(c, x0)
end