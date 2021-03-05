# Wiktoria Byra, 250131, Obliczenia naukowe - laboratorium 4, kod źródłowy do zadań 1, 2, 3 i 4

module Functions   
    using PyPlot

    function ilorazyRoznicowe(x::Vector{Float64}, f::Vector{Float64})
        len = length(f)
        fx = copy(f)
        for i in 2:len
            for j = len:-1:i
                fx[j] = (fx[j]-fx[j-1])/(x[j]-x[j-i+1])
            end
        end
        return fx
    end

    function warNewton(x::Vector{Float64}, fx::Vector{Float64}, t::Float64)
        len = length(x)
        nt = fx[len]
        for i in (len-1):(-1):1
            nt = fx[i]+(t-x[i])*nt
        end
        return nt
    end

    function naturalna(x::Vector{Float64}, fx::Vector{Float64})
        len = length(x)
        a = zeros(len)
        a[len] = fx[len]
        for i in (len-1):(-1):1
            a[i] = fx[i]-a[i+1]*x[i]
            for j in (i+1):(len-1)
                a[j] = a[j]-a[j+1]*x[i]
            end
        end
        return a
    end

    function rysujNnfx(f, a::Float64, b::Float64, n::Int)
        filename = "$(f)_[$(a),$(b)]_$(n)"
        nodes = n + 1
        x = zeros(nodes)
        y = zeros(nodes)
        fx = zeros(nodes)
        h = (b - a) / n
        arg = a
        l = 40
        plot_x = zeros(l * nodes)
        plot_f = zeros(l * nodes)
        plot_w = zeros(l * nodes)
        for i in 1:nodes
            x[i] = arg
            y[i] = f(arg)
            arg += h
        end
        fx = ilorazyRoznicowe(x, y)
        arg = a
        nodes *= l
        h = (b - a) / (nodes - 1)
        for i in 1:nodes
            plot_x[i] = arg
            plot_w[i] = warNewton(x, fx, arg)
            plot_f[i] = f(arg)
            arg += h
        end
        clf()
        plot(plot_x, plot_f, label = "f(x)", linewidth = 3)
        plot(plot_x, plot_w, label = "w(x)", linewidth = 1.5)
        legend(loc = 2, borderaxespad = 0)
        savefig("$(filename).png")
    end
    export ilorazyRoznicowe, warNewton, naturalna, rysujNnfx
end