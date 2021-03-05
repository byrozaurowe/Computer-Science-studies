def encode_code(binary_code):
    table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    encoded_output = ''
    while binary_code != '':
        if len(binary_code) < 6:
            while len(binary_code) != 6:
                binary_code += '0'
        encoded_output += table[encode_pack(binary_code[0:6])]
        binary_code = binary_code[6:len(binary_code)]
    return encoded_output


def encode_pack(six_bytes):
    number = 0
    power = 1
    while six_bytes != '':
        if six_bytes[len(six_bytes)-1] == '1':
            number += power
        power *= 2
        six_bytes = six_bytes[0:(len(six_bytes)-1)]
    return number


def decode_code(code):
    output_message = ''
    table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    dictionary = {}
    counter = 0
    for i in table:
        dictionary[i] = counter
        counter += 1
    binary_number = ''
    while code != '':
        number = dictionary[code[0]]
        for i in range(6):
            if number >= 2**(5-i):
                number -= 2**(5-i)
                binary_number += '1'
            else:
                binary_number += '0'
        code = code[1:len(code)]
    while len(binary_number) > 7:
        output_message += decode_pack(binary_number[0:8])
        binary_number = binary_number[8:len(binary_number)]
    return output_message


def decode_pack(eight_bytes):
    number = 0
    for i in range(8):
        if eight_bytes[i] == '1':
            number += 2**(7-i)
    return chr(number)


def read_input():
    binary_code = ''
    file = open("/home/byrka/Python/Lista_2/plik.bin", 'rb')
    byte = file.read(1)
    while byte != b"":
        binary_code += '0'
        binary_code += ''.join(format(ord(byte), 'b'))
        byte = file.read(1)
    return binary_code


def main():
    binary_input = ''
    encoded_output = ''
    decoded_output = ''

    binary_input = read_input()
    encoded_output = encode_code(binary_input)
    decode_code(encoded_output)
    decoded_output = decode_code(encoded_output)

    print(encoded_output)
    print(decoded_output)


if __name__ == "__main__":
    main()
