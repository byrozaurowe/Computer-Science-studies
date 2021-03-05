# Wiktoria Byra, zadanie 5 lista 2 laboratorium Obliczenia naukowe

# rekurenkcyjne obliczanie wartości funkcji
function rek(p, r, n)
    if n == 0
        return p
    else 
        pom = rek(p, r, n-1)
        return pom + r*pom*(1-pom)
    end
end

# wywołanie funkcji rekurencyjnej dla odpowiednich argumentów
function model(type_arg, p, n)
    p0::type_arg = p
    r::type_arg = 3
    return rek(p0, r, n)
end

function main()
    p0 = 0.01
    zaokr = floor(model(Float32, p0, 10), digits=3) # obcięta wartość funkcji po 10 iteracjach
    println("1. ")
    println("z zaokrągleniem po 10-tej iteracji: ", model(Float32, zaokr, 30))
    println("bez zaokrąglenia: ", model(Float32, p0, 40))
    println("2. ")
    println("Float64: ", model(Float64, p0, 40))
    println("Float32: ", model(Float32, p0, 40))
end