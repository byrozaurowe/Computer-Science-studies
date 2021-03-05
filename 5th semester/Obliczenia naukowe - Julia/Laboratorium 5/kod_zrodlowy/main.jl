# Wiktoria Byra, 250131, Obliczenia naukowe -laboratorium 5, funkcja testująca działanie modułu blocksys

include("./matrixgen.jl")
include("./blocksys.jl")
using .matrixgen
using .blocksys
using SparseArrays
using Plots

function gaussEliminationTest(M::SparseMatrixCSC{Float64,Int64}, b::Vector{Float64}, n::Int64, l::Int64)
    matrixAfterGaussB, bAfterGaussB = blocksys.gaussElimination(M, b, n, l)
    result = blocksys.solveGauss(matrixAfterGaussB, bAfterGaussB, n, l)
    return result
end

function gaussEliminationWithPartChoiceTest(M::SparseMatrixCSC{Float64,Int64}, b::Vector{Float64}, n::Int64, l::Int64) 
    matrixAfterGaussB, bAfterGaussB, pivots = blocksys.gaussEliminationWithPartChoice(M, b, n, l)
    result = blocksys.solveGaussWithPartChoice(matrixAfterGaussB, bAfterGaussB, n, l, pivots)
    return result
end

function linearEquation(M, b::Vector{Float64})
    return M\b
end

function testFromFile(matrixFile::String, bFile::String)
        time = zeros(Float64, 5)
        memory = zeros(Float64, 5)

        # test Gauss z generowaniem prawego wektora bez częściowego wyboru
        matrix = blocksys.matrixFromFile(matrixFile)
        b = blocksys.calculateRightVector(matrix[1], matrix[2], matrix[3])
        result = @time gaussEliminationTest(matrix[1], b, matrix[2], matrix[3])
        blocksys.saveToFile("bGeneratedOut.txt", result, matrix[2], true)
    
        # test Gauss bez generowania prawego wektora bez częściowego wyboru
        matrix = blocksys.matrixFromFile(matrixFile)
        b = blocksys.vectorFromFile(bFile)
        result = @time gaussEliminationTest(matrix[1], b, matrix[2], matrix[3])
        blocksys.saveToFile("bNotGeneratedOut.txt", result, matrix[2], false)
    
        # test Gauss z generowaniem prawego wektora z częściowym wyborem
        matrix = blocksys.matrixFromFile(matrixFile)
        b = blocksys.calculateRightVector(matrix[1], matrix[2], matrix[3])
        result = @time gaussEliminationWithPartChoiceTest(matrix[1], b, matrix[2], matrix[3])
        blocksys.saveToFile("bGeneratedPivotsOut.txt", result, matrix[2], true)
    
        # test Gauss bez generowania prawego wektora z częściowym wyborem
        matrix = blocksys.matrixFromFile(matrixFile)
        b = blocksys.vectorFromFile(bFile)
        result = @time gaussEliminationWithPartChoiceTest(matrix[1], b, matrix[2], matrix[3])
        blocksys.saveToFile("bNotGeneratedPivotsOut.txt", result, matrix[2], false)

        """# x = A/b
        matrix = blocksys.matrixFromFile(matrixFile)
        fullMatrix = SparseArrays.Matrix(matrix[1])
        b = blocksys.vectorFromFile(bFile)
        result = @time linearEquation(fullMatrix, b)"""

end

function testFromSampleFiles()
    testFromFile("16/A.txt", "16/b.txt")
    testFromFile("10000/A.txt", "10000/b.txt")
    testFromFile("50000/A.txt", "50000/b.txt")
end

# funkcja testująca czas wykonania funkcji dla dużego przekroju danych
function testTime()
    m = 1000
    gaussTime = zeros(Float64, m)
    gaussWithPartChoiceTime = zeros(Float64, m)

    for i in 1:m
        matrixgen.blockmat((i*20)+12, 4 ,10.0, "A.txt")
        matrix = blocksys.matrixFromFile("A.txt")
        b = blocksys.calculateRightVector(matrix[1], matrix[2], matrix[3])
        gaussTime[i] = @elapsed gaussEliminationTest(matrix[1], b, matrix[2], matrix[3])

        matrixgen.blockmat((i*20)+12, 4 ,10.0, "A.txt")
        matrix = blocksys.matrixFromFile("A.txt")
        b = blocksys.calculateRightVector(matrix[1], matrix[2], matrix[3])
        gaussWithPartChoiceTime[i] = @elapsed gaussEliminationWithPartChoiceTest(matrix[1], b, matrix[2], matrix[3])
    end

    x = zeros(Float64, m)
    for i = 1:m
        x[i] = (i*20)+12
    end
    plot(x, gaussTime, title = "Czas wykonania funkcji", label = "bez wyboru elementu głównego", ylabel = "czas (s)", xlabel = "rozmiar macierzy")
    plot!(x, gaussWithPartChoiceTime, label = "z częściowym wyborem elementu głównego")
    savefig("time.png")
end

function testMemory()
    m = 1000
    gaussTime = zeros(Float64, m)
    gaussWithPartChoiceTime = zeros(Float64, m)

    for i in 1:m
        matrixgen.blockmat((i*20)+12, 4 ,10.0, "A.txt")
        matrix = blocksys.matrixFromFile("A.txt")
        b = blocksys.calculateRightVector(matrix[1], matrix[2], matrix[3])
        gaussTime[i] = @allocated gaussEliminationTest(matrix[1], b, matrix[2], matrix[3])

        matrixgen.blockmat((i*20)+12, 4 ,10.0, "A.txt")
        matrix = blocksys.matrixFromFile("A.txt")
        b = blocksys.calculateRightVector(matrix[1], matrix[2], matrix[3])
        gaussWithPartChoiceTime[i] = @allocated gaussEliminationWithPartChoiceTest(matrix[1], b, matrix[2], matrix[3])
    end

    x = zeros(Float64, m)
    for i = 1:m
        x[i] = (i*20)+12
    end
    p = plot(x, gaussTime, title = "Pamięć alokowana przez funkcję", label = "bez wyboru elementu głównego", ylabel = "pamięć (bytes)", xlabel = "rozmiar macierzy")
    plot!(x, gaussWithPartChoiceTime, label = "z częściowym wyborem elementu głównego")
    savefig("memory.png")
end

function main()
    #testFromFile()
    #testMemory()
    #testTime()
end