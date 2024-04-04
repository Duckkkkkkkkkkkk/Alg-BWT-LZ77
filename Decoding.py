def calculate_text_length_in_bits(text):
    return len(text) * 16


def decodeLZ77(encoded_text):
    decoded_text = ""
    current_tuple = None

    for line in encoded_text:
        line = line.strip()
        if line.startswith('(') and line.endswith(')'):
            # Complete tuple on a single line
            current_tuple = eval(line)
            offset, length, char = current_tuple
            if offset == 0:
                decoded_text += char
            else:
                start = len(decoded_text) - offset
                end = start + length
                decoded_text += decoded_text[start:end] + char
        elif current_tuple is not None:
            # Continue tuple from the previous line
            current_tuple += eval(line)
            offset, length, char = current_tuple
            start = len(decoded_text) - offset
            end = start + length
            decoded_text += decoded_text[start:end] + char

    return decoded_text


def main(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        encoded_text = file.readlines()

    decoded_text = decodeLZ77(encoded_text)

    decoded_lz77_text_length = len(decoded_text) * 8
    #print(f"Длина текста, декодированного алгоритмом LZ77: {decoded_lz77_text_length} бит")

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(decoded_text)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def addAtLast(head, nn):
    if head is None:
        head = nn
        return head
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = nn
    return head


def computeLShift(head, index, l_shift):
    l_shift[index] = head.data
    head = head.next


def cmpfunc(a, b):
    return ord(a) - ord(b)


def invert(bwt_arr):
    len_bwt = len(bwt_arr)
    sorted_bwt = sorted(bwt_arr)

    try:
        # Find the position of the end-of-text marker ('$') in the original BWT
        original_end_marker_position = bwt_arr.index('$')
    except ValueError:
        original_end_marker_position = 0

    # Create arr dynamically based on the characters present in bwt_arr
    unique_chars = sorted(set(bwt_arr))
    arr = {char: [] for char in unique_chars}

    for i in range(len_bwt):
        arr[bwt_arr[i]].append(i)

    l_shift = [0] * len_bwt

    for i in range(len_bwt):
        l_shift[i] = arr[sorted_bwt[i]].pop(0)

    decoded = [''] * len_bwt
    x = original_end_marker_position  # Start decoding from the original end-of-text marker position
    for i in range(len_bwt):
        x = l_shift[x]
        decoded[len_bwt - 1 - i] = bwt_arr[x]

    decoded_str = ''.join(decoded)

    return decoded_str

def decode_and_write(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        bwt_arr = file.read().strip()

    decoded_str = invert(bwt_arr)

    decoded_length_bits = len(decoded_str) * 8
    #print(f"Длина текста, декодированного алгоритмом Барроуза-Уиллера: {decoded_length_bits} бит")
    print(f"Длина декодированного текста: {decoded_length_bits} бит")

    decoded_str_without_marker = decoded_str.replace('$', '')

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(decoded_str_without_marker[::-1])


if __name__ == "__main__":
    input1_file = 'C:/Users/Анастасия/Desktop/3 course/codingTheory/ArchivatorLab1/mumu_encoding.txt'
    input2_file = 'C:/Users/Анастасия/Desktop/3 course/codingTheory/ArchivatorLab1/mumu_decoding.txt'
    output_file = 'C:/Users/Анастасия/Desktop/3 course/codingTheory/ArchivatorLab1/mumu_decoding.txt'

    main(input1_file, output_file)
    decode_and_write(input2_file, output_file)

    print("Декодированный текст был записан в файл", output_file)
