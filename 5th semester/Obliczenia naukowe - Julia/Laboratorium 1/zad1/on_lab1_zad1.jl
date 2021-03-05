# Wiktoria Byra, zadanie 1 lista 1 laboratorium Obliczenia naukowe

# funkcja obliczająca epsilon maszunowy dla danego typu
function macheps(type_arg)
	prev::type_arg = 0.5
	test::type_arg = 0.5
	# zaczynamy poczukiwanie macheps od 0.5 i zmniejszamy dwukrotnie, dopóki liczba nie będzie tak mała, że po dodadniu do 1 wynik zaokrągli się do 1
	while type_arg(1+test) != 1
        prev = test; 
        test /= 2; 
	end
	# wypisanie macheps znalezionego przez funkcję
	println("macheps = ", prev)
	# wypisanie macheps znalezionego przez wbudowaną funkcję języka julia
	println("eps = ", eps(type_arg))
end

# funkcja obliczjąca liczbę eta > 0.0 dla danego typu
function eta(type_arg)
	max::type_arg = 1.0
	min::type_arg = 0.0
	two::type_arg = 2.0
	test::type_arg = 0.0
	# eta znajduje się pomiędzy 0.0 a 1.0
	for i = 1:10000
		# wyznaczamy średnia z dolnego i górnego ograniczenia
		test = (max + min) / two
		# jeżeli średnia jest zaokrąglana do 0 musimy znaleźć większą liczbę, więc przesuwamy done ograniczenie
		if test == 0.0
			min = test
		# w przeciwnym przypadku szukana liczba może być równa średnie lub mniejsza, więc przesuwamy górne ograniczenie na średnią
		else
			max = test
		end
	end
	# wypisanie ety znalezionej przez program
	println("eta = ", max)
	# wypisanie ety obliczonej za pomocą wbudowanej funkcji języka julia
	println("nextfloat = ", nextfloat(type_arg(0.0)))
end

# funkcja wyznaczająca górny zakres danego typu
function max(type_arg)
    max::type_arg = nextfloat(type_arg(0.0))
	min::type_arg = 0.0
	# zaczynamy od najmniejszej liczby i zwiększamy ją dwukrotnie, dopóki nie znajdziemy się w infinity, wtedy wiemy, że max zanjduje się pomiędzy ostatnią liczbą, która nie leżała w nieskończoności a jej dwukrotnością
    while isinf(max) == false
        min = max
        max = 2.0 * max
    end
    mid::type_arg = 3.0 * min / 2.0
	diff::type_arg = min
	two::type_arg = 2.0
	# następnie poszukujemy maksimum za pomocą binsearcha
    while isinf(nextfloat(type_arg(mid))) == true || isinf(mid) == false
		if isinf(nextfloat(type_arg(mid))) == false
            diff  = diff / two
            if min != mid
                min = mid
            else 
                mid = nextfloat(type_arg(mid))
                break
            end
		else
			diff = diff / two
        end
		mid = min + diff
    end
	# wypisanie max znalezionego przez program
	println("max = ", mid)
	# wypisanie max znalezionego przez wbudowaną funkcję języka julia
    println("floatmax = ", floatmax(type_arg))
end

function main()
	macheps(Float16)
	macheps(Float32)
	macheps(Float64)
	eta(Float16)
	eta(Float32)
	eta(Float64)
	max(Float16)
	max(Float32)
	max(Float64)
end
