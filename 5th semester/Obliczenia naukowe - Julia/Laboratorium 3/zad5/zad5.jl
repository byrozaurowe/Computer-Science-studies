# autor: Wiktoria Byra, zadanie 5 lista 3 Obliczenia naukowe

function f(x) # róznica pomiędzy funkcjami, których miejsca przecięcia szukamy
    return MathConstants.e^x - 3x
end

function main()
    delta = 10^(-4)
    epsilon = 10^(-5)
    print(mbisekcji(f, 0.0, 1.0, delta, epsilon), "\n")
    print(mbisekcji(f, 1.0, 2.0, delta, epsilon))
end