# Wiktoria Byra, zadanie 1 lista 2 laboratorium Obliczenia naukowe

# fukncja obliczająca iloczyn skalarny
function scalar_prod(type_arg, n)
    # wektory, składniki iloczynu
    x::Vector{type_arg} = [2.718281828, -3.141592654, 1.414213562, 0.577215664, 0.301029995]
    y::Vector{type_arg} = [1486.2497, 878366.9879, -22.37492, 4773714.647, 0.000185049]
    # tutaj będą zapisane wyniki iloczynu dla 4 różnych metod
    res1::type_arg = 0.0
    res2::type_arg = 0.0
    res3::type_arg = 0.0
    res4::type_arg = 0.0
    # obliczanie iloczynu sumując iloczyny po kolei
    for i = 1:n
        res1 += x[i] * y[i]
    end
    # obliczanie iloczynu sumując iloczyny od końca wektora
    for i = 1:n
        res2 += x[n+1-i] * y[n+1-i]
    end
    # obliczanie iloczynu sumując iloczyny od największego do najmniejszego, ujemne od najmniejszego do największego
    for i = 1:n
        x[i] = x[i] * y[i]
    end
    sum_pos::type_arg = 0.0 # tutaj będzie zapisana suma dodatnich iloczynów
    sum_neg::type_arg = 0.0 # tutaj będzie zapisana suma ujemnych iloczynów
    # posortowanie tablicy iloczynów malejąco
    sort!(x, rev = true)
    # zsumowanie dodatnich
    for i = 1:n
        if x[i] < 0 
            break
        end
        sum_pos += x[i]
    end
    # zsumowanie ujemnych
    for i = 1:n
        if x[n+1-i] >= 0
            break
        end
        sum_neg += x[n+1-i]
    end
    res3 = sum_neg + sum_pos
    # obliczanie iloczynu sumując iloczyny od najmnijeszego do największego, a ujemne od największego do najmniejszego
    sum_pos = 0.0
    sum_neg = 0.0
    # zsumowanie dodatnich iloczynow w kolejności rosnącej
    for i = 1:n
        if x[n+1-i] >= 0
            sum_pos += x[n+1-i]
        end
    end
    # zsumowanie ujemnych iloczynów w kolejności malejącej
    for i = 1:n
        if x[i] < 0
            sum_neg += x[i]
        end
    end
    res4 = sum_neg + sum_pos
    # wyoisanie wyników iloczynu skalarnego obliczonego 4 sposobami
    println("sposób 1: wynik = ", res1)
    println("sposób 2: wynik = ", res2)
    println("sposób 3: wynik = ", res3)
    println("sposób 4: wynik = ", res4)
end

function main()
    scalar_prod(Float32, 5)
    scalar_prod(Float64, 5)
end
