# Wiktoria Byra, zadanie 3 lista 1 laboratorium Obliczenia naukowe

# funkcja wypisująca wykładnik potęgi 2 w standardzie double IEEE754 dla liczb z przedziału 1-2
function delta()
    start::Float64 = nextfloat(Float64(1.0))
    while start <= 2.0
        println(SubString(bitstring(start), 2:12))
        start = nextfloat(Float64(start))
    end
end

# funkcja wypisująca wykładnik potęgi 2 w standardzie double IEEE754 dla liczb z przedziału 1/2-1
function delta2()
    start::Float64 = nextfloat(Float64(0.5))
    while start <= 1.0
        println(SubString(bitstring(start), 2:12))
        start = nextfloat(Float64(start))
    end
end

# funkcja wypisująca wykładnik potęgi 2 w standardzie double IEEE754 dla liczb z przedziału 2-4
function delta3()
    start::Float64 = nextfloat(Float64(2.0))
    while start <= 4.0
        println(SubString(bitstring(start), 2:12))
        start = nextfloat(Float64(start))
    end
end