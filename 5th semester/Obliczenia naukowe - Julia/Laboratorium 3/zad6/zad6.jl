# autor: Wiktoria Byra, zadanie 6 lista 3 Obliczenia naukowe

function f1(x)
    return MathConstants.e^(1-x)-1
end

function pf1(x) # pochodna funkcji f1(x)
    return -MathConstants.e^(1-x)
end

function f2(x)
    x*MathConstants.e^(-x)
end

function pf2(x) # pochodna funkcji f2(x)
    return -MathConstants.e^(-x)*(x-1)
end

function main()
    delta = 10^(-5)
    epsilon = delta
    maxit = 1000
    
    print("funkcja f1 \n")

    print("metoda bisekcji \n")
    intervals = [(0.0, 2.0), (-2.0, 2.0), (0.1, 1.8), (0.1, 1.2), (-0.2, 1.8), (-5.0, 500.0)]
    for iv in intervals
        (r, v, it, err) = mbisekcji(f1, iv[1], iv[2], delta, epsilon)
        print("[", iv[1], ",", iv[2], "]: ", (r, v, it, err), "\n")
    end

    print("metoda stycznych \n")
    starts = [-1.0, 0.0, 1.1, 2.0, 6.0, 8.0, 15.00]
    for s in starts
        (r, v, it, err) = mstycznych(f1, pf1, s, delta, epsilon, maxit)
        print("x0 = ", s, ": ", (r, v, it, err), "\n")
    end

    print("metoda siecznych: \n")
    starts = [(-2.0, 2.0), (-0.3, 1.8), (0.1, 1.3), (-2.0, 6.0), (-10.0, 10.0), (10.0, 100.0)]
    for s in starts
        (r, v, it, err) = msiecznych(f1, s[1], s[2], delta, epsilon, maxit)
        print("x0 = ", s[1],", x1 = ", s[2], ": ", (r, v, it, err), "\n")
    end

    print("funkcja f2 \n")

    print("metoda bisekcji \n")
    intervals = [(-0.5, 0.5), (-0.7, 0.4), (-10.0, 100.)]
    for iv in intervals
        (r, v, it, err) = mbisekcji(f2, iv[1], iv[2], delta, epsilon)
        print("[", iv[1], ",", iv[2], "]: ", (r, v, it, err), "\n")
    end

    print("metoda stycznych \n")
    starts = [-1.0, -0.4, 0.0, 1.0, 6.0, 8.0, 15.00]
    for s in starts
        (r, v, it, err) = mstycznych(f2, pf2, s, delta, epsilon, maxit)
        print("x0 = ", s, ": ", (r, v, it, err), "\n")
    end

    print("metoda siecznych \n")
    starts = [(-2.0, 2.0), (-0.3, 1.8), (0.1, 1.3), (-2.0, 6.0), (-10.0, 10.0), (10.0, 100.0)]
    for s in starts
        (r, v, it, err) = msiecznych(f2, s[1], s[2], delta, epsilon, maxit)
        print("x0 = ", s[1],", x1 = ", s[2], ": ", (r, v, it, err), "\n")
    end
end