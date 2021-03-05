import zlib
import sys


def crc(text):
    crc_code = str("{0:b}".format(zlib.crc32(text.encode())))
    new_text = '0' * (32 - len(crc_code)) + crc_code
    return new_text


def bit_stuff(text):
    ones_counter = 0
    new_text = ''
    for i in range (len(text)):
        new_text += text[i]
        if text[i] == '0':
            ones_counter = 0
        if text[i] == '1':
            ones_counter += 1
            if ones_counter == 5:
                new_text += '0'
                ones_counter = 0
    return new_text


def encode_file(text):
    FLAG = '01111110'
    return FLAG + bit_stuff(text + crc(text)) + FLAG


def crc_check(text):
    content = text[0:(-32)]
    count_crc = str("{0:b}".format(zlib.crc32(content.encode())))
    crc_pattern =  '0' * (32 - len(count_crc)) + count_crc
    if crc_pattern != text[(-32):]:
        print("crc wrong")
        return None
    else:
        #print("crc check")
        return content


def bit_unstuff(text):
    ones_counter = 0
    new_text = ''
    for i in range (len(text)):
        if text[i] == '1':
            ones_counter += 1
            new_text += '1'
        if text[i] == '0':
            if ones_counter != 5:
                new_text += '0'
            ones_counter = 0
    return new_text


def decode_file(text):
    decoded = crc_check(bit_unstuff(text))
    if decoded:
        print(decoded)
        return 1
    else:
        return 0


def main():
    file_in = sys.argv[1]
    file_out = sys.argv[2]
    frame_counter = 0
    FLAG = '01111110'
    frame_size = 50
    '''with open(file_in) as z:
        text = z.read().strip()
        z.close()
        with open(file_out, "w+") as w:
            if len(text) != 0:
                i = frame_size
                while i < len(text):
                    frame_counter += 1
                    w.write(encode_file(text[(i-frame_size):i]))
                    i += frame_size
                frame_counter += 1
                w.write(encode_file(text[(i-frame_size):]))
                w.close()
                print(frame_counter) '''
    with open(file_out) as w:
        text = w.read()
        w.close()
        start_flag = False
        end_flag = False
        i = 0
        j = 0
        frame_counter = 0
        while (i + 8) <= len(text):
            if text[i:(i+8)] == FLAG:
                if start_flag == False:
                    if end_flag == False:
                        start_flag = True
                        j = i
                    else:
                        end_flag = False
                else:
                    end_flag = True
            if start_flag == True and end_flag == True:
                frame_counter += 1
                check = decode_file(text[(j + 8):i])
                if check == 1:
                    start_flag = False
                    end_flag = False
                else:
                    start_flag = False
            i += 1
        print(frame_counter)


if __name__ == "__main__":
    main()