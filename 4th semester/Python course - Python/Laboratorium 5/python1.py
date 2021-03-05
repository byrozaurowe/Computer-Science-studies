import csv
import numpy as np
import matplotlib.pyplot as plt


def main():
    """print("ścieżka do pliku z filmami: ")
    movies_file_path = input()
    print("ścieżka do pliku z ocenami: ")
    ratings_file_path = input()
    print("tytuł szukanego filmu: ")
    movie_name = input()"""

    # ścieżki do plików z filmami i z ocenami filmów, pliki musza się znajdować w tym folderze co program
    movies_file_path = "movies.csv"
    ratings_file_path = "ratings.csv"
    # szukany film
    movie_name = "Toy Story"
    
    # liczba filmów, na podstawie których będzie obliczana przewidywana ocena
    print("m = ")
    m = int(input())
    # liczba osób, na podstawie których ocen będzie wyliczana przewidywana ocena
    print("i = ")
    i = int(input())

    # wyszukiwanie id filmu na pdst. tytułu
    movie_id = 0
    with open(movies_file_path, 'r', encoding = 'utf-8') as movies_file:
        csvreader = csv.reader(movies_file)
        for row in csvreader:
            if movie_name in row[1]:
                movie_id = int(row[0])
                break
    if movie_id == 0:
        print("brak filmu w bazie!")

    else:
        # macierz, w której będą oceny filmów wystawione przez użytkowników
        X = []
        # tabela, w której będą oceny filmu Toy Story
        Y = []
        # nowe indeksy użytkowników, tylko tych którzy ocenili Toy Story
        users = {}
        for k in range (i):
            X.append([0 for j in range (m)])
        # wyszukiwanie użytkowników, którzy ocenili Toy Story
        with open(ratings_file_path, 'r', encoding = 'utf-8') as ratings_file:
            csvreader = csv.reader(ratings_file)
            j = 0
            for row in csvreader:
                if j == 0:
                    j += 1
                    continue
                if int(row[1]) == movie_id:
                    Y.append([float(row[2])])
                    users[row[0]] = j - 1
                    j += 1
        # pobieranie ocen innych filmów
        with open(ratings_file_path, 'r', encoding = 'utf-8') as ratings_file:
            csvreader = csv.reader(ratings_file)
            for row in csvreader:
                if row[0] in users.keys() and int(row[1]) <= m + 1 and int(row[1]) != 1 and users[row[0]] < i:
                    X[users[row[0]]][int(row[1]) - 2] = float(row[2])

    # oblicznie predykcji
    x = np.array(X)
    y = np.array(Y)
    A = np.hstack([x, np.ones((x.shape[0], 1))])
    reg = np.linalg.lstsq(A, y)[0]
    out = np.dot(A, reg)
    print(out)
    
    # rysowanie wykresu
    plt.plot(out, 'm', label = "regresja")
    # prawdziwe oceny Tooy Story
    plt.plot(Y, 'o', label = "oryginalne oceny")
    plt.legend()
    plt.show()


# uruchamianie funkcji main przy włączeniu programu
if __name__ == "__main__":
    main()