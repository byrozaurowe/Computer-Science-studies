# Wiktoria Byra, zadanie 2 lista 1 laboratorium Obliczenia naukowe

# funkcja obliczająca epsilon maszynowy za pomoca wyrażenia Kahana
function kahan(type_arg)
    one::type_arg = 1.0
    three::type_arg = 3.0
    four::type_arg = 4.0
    result::type_arg = (four / three - one) * three - one
    println("result = ", result)
    println("eps = ", eps(type_arg))
end

function main()
    kahan(Float16)
    kahan(Float32)
    kahan(Float64)
end