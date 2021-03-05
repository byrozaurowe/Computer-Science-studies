# Wiktoria Byra, 250131, Obliczenia naukowe - laboratorium 4, funkcja testująca funkcje ilorazyRoznicowe, warNewton, naturalna

include("./func.jl")
using .Functions
function main()
    x = [1.0, 2.0, 8.0, 0.5, 5.0]
    f = [1.0, -3.0, -9.0, -0.5, 2.0]
    println("test ilorazy różnicowe: ", ilorazyRoznicowe(x, f))
    println("test war newton: ", warNewton(x,f,1.0))
    println("test war newton: ", warNewton(x,f,8.0))
    println("test naturalna: ", naturalna(x,f))
end