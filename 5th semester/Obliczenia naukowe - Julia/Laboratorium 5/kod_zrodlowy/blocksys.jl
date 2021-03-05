# Wiktoria Byra, 250131, Obliczenia naukowe -laboratorium 5, moduł blocksys

module blocksys

export matrixFromFile, vectorFromFile, calculateRightVector, gaussElimination, solveGauss, gaussEliminationWithPartChoice, saveToFile

using SparseArrays
using LinearAlgebra

function matrixFromFile(filePath::String)::Tuple{SparseMatrixCSC{Float64,Int64}, Int64, Int64}
    out = C_NULL
    
    open(filePath, "r") do file
        columns = []
        rows = []
        values = []
        firstLine = split(readline(file))
        n = parse(Int64, firstLine[1]) # rozmiar macierzy A
        l = parse(Int64, firstLine[2]) # rozmiar macierzy Ak, Bk, Ck

        for line in eachline(file)
            words = split(line)
            push!(rows, parse(Int64, words[1]))
            push!(columns, parse(Int64, words[2]))
            push!(values, parse(Float64, words[3]))
        end

        A = sparse(rows, columns, values)
        out = (A, n, l)
    end

    return out
end

function vectorFromFile(filePath::String)::Array{Float64,1}
    vector = []

    open(filePath, "r") do file
        n = parse(Int64, readline(file)) # rozmiar wektora b

        for line in eachline(file)
            push!(vector, parse(Float64, line))
        end
    end
    
    return vector
end

function calculateRightVector(M::SparseMatrixCSC{Float64,Int64}, n::Int64, l::Int64)
    vector = zeros(Float64, n)

    for i in 1:n
        for j in (max(i - l, 1)):(min(i + l, n))
            vector[i] += M[i, j]
        end
    end
        
    return vector
end

function gaussElimination(M::SparseMatrixCSC{Float64,Int64}, b::Vector{Float64}, n::Int64, l::Int64)
    for k in 1:n-1
        for i in k+1:min(n, k + l)
            z = M[i, k] / M[k, k]
            M[i, k] = 0.0

            for j in k+1:min(n, k + l)
                M[i, j] -= z * M[k, j]
            end

            b[i] -= z * b[k]
        end
    end
    return M, b
end

function solveGauss(M::SparseMatrixCSC{Float64,Int64}, b::Vector{Float64}, n::Int64, l::Int64)::Vector{Float64}
    result = zeros(Float64, n)

    for i in n:-1:1
        currentSum = 0
        for j in i + 1:min(n, i + l)
            currentSum += M[i, j] * result[j]
        end

        result[i] = (b[i] - currentSum) / M[i, i]
    end

    return result
end

function gaussEliminationWithPartChoice(M::SparseMatrixCSC{Float64,Int64}, b::Vector{Float64}, n::Int64, l::Int64)
    pivots = zeros(Int64, n)

    for i in 1:n
        pivots[i] = i
    end

    for k in 1:n-1
        lastColumn = 0
        lastRow = 0

        for i in k:min(n, k + l)
            if abs(M[pivots[i], k]) > lastColumn
                lastColumn = abs(M[pivots[i], k])
                lastRow = i
            end
        end

        pivots[lastRow], pivots[k] = pivots[k], pivots[lastRow]

        for i in k+1:min(n, k + l)
            z = M[pivots[i], k] / M[pivots[k], k]
            M[pivots[i], k] = 0.0

            for j in k+1:min(n, k + 2 * l)
                M[pivots[i], j] = M[pivots[i], j] - z * M[pivots[k], j]
            end
            b[pivots[i]] = b[pivots[i]] - z * b[pivots[k]]
        end
    end

    return M, b, pivots
end

function solveGaussWithPartChoice(M::SparseMatrixCSC{Float64, Int64}, b::Vector{Float64}, n::Int64, l::Int64, pivots::Vector{Int64})::Vector{Float64}
    result = zeros(Float64, n)
    
    for k in 1:n-1
        for i in k+1:min(n, k + 2 * l)
            b[pivots[i]] = b[pivots[i]] - M[pivots[i], k] * b[pivots[k]]
        end
    end

    for i in n:-1:1
        currentSum = 0
        for j in i+1:min(n, i + 2 * l)
            currentSum += M[pivots[i], j] * result[j]
        end
        result[i] = (b[pivots[i]] - currentSum) / M[pivots[i], i]
    end

    return result
end

function saveToFile(filePath::String, x::Vector{Float64}, n::Int64, isRightGenerated::Bool)
    open(filePath, "w") do file
        o = ones(Float64, n)
        relativeError = norm(o - x) / norm(x)
        print("n - ", n, ": ", relativeError)
        if (isRightGenerated == true)
            println(file, relativeError)
        end

        for i = 1:n
            println(file, x[i])
        end
    end
end

end