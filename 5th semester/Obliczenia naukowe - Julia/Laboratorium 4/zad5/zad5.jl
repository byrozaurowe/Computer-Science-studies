# Wiktoria Byra, 250131, Obliczenia naukowe - laboratorium 4, kod źródłowy do zadania 5

include("./func.jl")
using .Functions
function main()
    f = x -> exp(x)
    n = [5, 10, 15]
    for i in n 
        Functions.rysujNnfx(f, 0.0, 1.0, i)
    end
    f = x -> x^2 * sin(x)
    n = [5, 10, 15]
    for i in n 
        Functions.rysujNnfx(f, -1.0, 1.0, i)
    end
end