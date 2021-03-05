# Wiktoria Byra, zadanie 3 lista 2 laboratorium Obliczenia naukowe

function hilb(n::Int)
    # Function generates the Hilbert matrix  A of size n,
    #  A (i, j) = 1 / (i + j - 1)
    # Inputs:
    #	n: size of matrix A, n>=1
    #
    #
    # Usage: hilb(10)
    #
    # Pawel Zielinski
            if n < 1
             error("size n should be >= 1")
            end
            return [1 / (i + j - 1) for i in 1:n, j in 1:n]
    end

using LinearAlgebra
function matcond(n::Int, c::Float64)
# Function generates a random square matrix A of size n with
# a given condition number c.
# Inputs:
#	n: size of matrix A, n>1
#	c: condition of matrix A, c>= 1.0
#
# Usage: matcond(10, 100.0)
#
# Pawel Zielinski
        if n < 2
         error("size n should be > 1")
        end
        if c < 1.0
        println("c = ", c)
         error("condition number  c of a matrix  should be >= 1.0")
        end
        (U,S,V)=svd(rand(n,n))
        return U*diagm(0 =>[LinRange(1.0,c,n);])*V'
end

# funkcja obliczająca błąd względny
function rel_error(res, x)
    return norm(res - x) / norm(x)
end

# funkcja obliczająca funkcję liniową z macierzy Hilberta
function linear_func_hilbert(m)
    for n = 2:m
        A = hilb(n) # generowanie macierzy Hilberta
        x = ones(n) # generowanie macierzy jednostkowej
        b = A * x
        i = LinearAlgebra.cond(A)
        println("n $n c $i ",rel_error(A\b,x), " ",  rel_error(inv(A)*b,x))
    end
end

# funkcja obliczająca funkcje liniową z losowej macierzy z danym wskaźnikiem uwarunkowania
function linear_func_random()
    n = [5, 10, 20]
    c = [1, 10, 10^3, 10^7, 1000000000000, 10000000000000000]
    for j in n
        for i in c
            A = matcond(j, Float64(i)) # generowanie macierzy losowej
            x = ones(j) # generowanie macierzy jednostkowej
            b = A * x
            println("n $j c $i ", rel_error(A\b,x), " ",  rel_error(inv(A)*b,x))
        end
    end
end

function main()
    println("macierz hilberta")
    linear_func_hilbert(20)
    println("losowe")
    linear_func_random()
end