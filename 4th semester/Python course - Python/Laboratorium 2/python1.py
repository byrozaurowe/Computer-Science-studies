import sys

path_to_file = str(sys.argv[1])

file = open(path_to_file)
file.seek(0, 2)
size_in_bytes = file.tell()
print("Liczba bajtow: ", size_in_bytes)

file = open(path_to_file)
words_counter = 0
lines_counter = 0
maximum_line_length = 0
for line in file:
    lines_counter += 1
    words_in_line = len(line.split())
    words_counter += words_in_line
    if (len(line.strip()) - line.count('\n')) > maximum_line_length:
        maximum_line_length = len(line) - line.count('\n')
print("Liczba slow: ", words_counter)
print("Liczba linii: ", lines_counter)
print("Maksymalna dlugosc linii: ", maximum_line_length)
