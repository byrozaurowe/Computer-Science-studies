# autor: Wiktoria Byra, zadanie 4 lista 3 Obliczenia naukowe

function f(x)
    return sin(x)-(1/2*x)^2
end

function pf(x) # pochodna funkcji f(x)
    return cos(x) - x/2
end

function main()
    print("metoda bisekcji: ", mbisekcji(f, 1.5, 2.0, 1/2*10^(-5), 1/2*10^(-5)), "\n")
    print("metoda stycznych: ", mstycznych(f, pf, 1.5, 1/2*10^(-5), 1/2*10^(-5), 1000), "\n")
    print("metoda siecznych: ", msiecznych(f, 1.0, 2.0, 1/2*10^(-5), 1/2*10^(-5), 1000), "\n")
end