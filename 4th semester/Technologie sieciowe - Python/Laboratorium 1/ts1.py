import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random


# generowanie grafu dwunastościennego, bez 1 krawędzi
def create_graph():
    G = nx.dodecahedral_graph()
    for e in G.edges:
        G.remove_edge(*e)
        break
    nx.draw(G)
    plt.show()
    return G

# generowanie macierzy natężeń
def create_intensity_matrix(size, max_n):
    N = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            if i!= j:
                N[i][j] = random.randint(0, max_n)
    return N

# funkcja a(e) - funkcja przepływu (pakiety na sekundę)
def a(G, N):
    nx.set_edge_attributes(G, 0, 'a')
    for i in range(len(N)):
        for j in range(len(N[i])):
            min_path = nx.shortest_path(G, i, j)
            for k in range(len(min_path) - 1):
                G[min_path[k]][min_path[k + 1]]['a'] += N[i][j]
    return G

# funkcja T - średnie opóźnienie pakietu w sieci
def T(C, N, m, c):
    G = N.sum()
    sum_e = np.sum([C.get_edge_data(*e).get('a') / (c / m - C.get_edge_data(*e).get('a')) for e in C.edges])
    #print("średnie opóźnienie: " + str(1 / G*sum_e))
    return (1 / G*sum_e)

def reliability(G, N, c, p, m, t_max, n = 1000):
    t = []
    for i in range(n):
        G_copy = nx.Graph(G)
        for e in G_copy.edges:
            if random.random() > p:
                G_copy.remove_edge(*e)
        if nx.is_connected(G_copy) == False:
            continue
        G_copy = a(G_copy, N) # generowanie funkcji przepływu
        is_a_good = True
        for e in G_copy.edges:
            if G_copy.get_edge_data(*e).get('a') >= c:
                is_a_good = False
                break
        if is_a_good:
            t_for_graph = T(G_copy, N, m, c)
            if t_for_graph < t_max:
                t.append(t_for_graph)
    print("niezawodność sieci: " + str(len(t)/n * 100) + "%")
    return len(t)/n * 100

def main():
    max_n = 50 # maksymalne natężenie
    c = 200000000 # funkcja przepustowości (max bity na sekundę w kanale komunikacyjnym), 200 mb/s
    p = 0.95 # prawdopodobieństwo nieuszkodzenia sieci
    m = 1500 # średnia wielkość pakietu w bitach
    t_max = 0.0004 # maksymalne opóźnienie pakietu w sieci

    G = create_graph()
    N = create_intensity_matrix(20, max_n) 
    
    # zwiększanie natężeń
    const = 1.1
    c_copy = 15000000
    N_copy = N.copy()
    reliab = []
    for i in range(20):
        for i in range(len(N_copy)):
            for j in range(len(N_copy)):
                N_copy[i][j] = int(N_copy[i][j] * const)
        reliab.append(reliability(G, N_copy, c_copy, p, m, t_max, 1000))
    plt.subplot(3, 1, 1)
    plt.plot([np.power(1.1, i) for i in range(20)], reliab, label = "niezawodność") 
    plt.xlabel("mnożnik elementów macierzy N")
    plt.legend()
    plt.subplots_adjust(bottom=0.5)

    # zwiększanie przepustowości
    const = 1.02
    reliab = []
    c_copy = 10000000
    for i in range(20):
        c_copy = c_copy * const
        reliab.append(reliability(G, N, c_copy, p, m, t_max, 1000))
    plt.subplot(3, 1, 2)
    plt.plot([100 * np.power(1.02, i) for i in range(20)], reliab, label = "niezawodność") 
    plt.xlabel("przepustowość c w Mb/s")
    plt.legend()
    plt.subplots_adjust(bottom=0.5)

    # dodawanie krawędzi
    G_copy = nx.Graph(G)
    reliab = []
    for i in range(20):
        v = random.randint(0, len(G_copy.nodes) - 1)
        w = random.randint(0, len(G_copy.nodes) - 1)
        while (G_copy.has_edge(v, w)):
            w = random.randint(0, len(G_copy.nodes) - 1)
        G_copy.add_edge(v, w)
        reliab.append(reliability(G_copy, N, c, p, m, t_max, 1000))
    plt.subplot(3, 1, 3)
    plt.plot([i for i in range(20)], reliab, label = "niezawodność") 
    plt.xlabel("liczba dodanych krawędzi") 
    plt.subplots_adjust(bottom=0.2)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()