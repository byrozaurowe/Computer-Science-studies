# Wiktoria Byra, zadanie 6 lista 1 laboratorium Obliczenia naukowe

# funkcja f(x) = sqrt(x^2 + 1) - 1
function f(n)
    eight::Float64 = 8.0
    for i = 1:n
        x::Float64 = eight ^ (-1 * i) # argument funkcji
        f::Float64 = sqrt(x * x + 1.0) - 1.0
        println("f(", x, ") = ", f)
    end
end

# funkcja g(x) = 2^2/(sqrt(x^2 + 1) + 1)
function g(n)
    eight::Float64 = 8.0
    for i = 1:n
        x::Float64 = eight ^ (-1 * i) # argument funkcji
        g::Float64 = x * x / (sqrt(x * x + 1.0) + 1.0)
        println("g(", x, ") = ", g)
    end
end

function main()
    f(10)
    g(10)
end