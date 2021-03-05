# Wiktoria Byra, 250131, Obliczenia naukowe - laboratorium 4, kod źródłowy do zadania 6

include("./func.jl")
using .Functions
function main()
    f = x -> abs(x)
    n = [5, 10, 15]
    for i in n 
        Functions.rysujNnfx(f, -1.0, 1.0, i)
    end
    f = x -> 1/(1+x^2)
    n = [5, 10, 15]
    for i in n 
        Functions.rysujNnfx(f, -5.0, 5.0, i)
    end
end