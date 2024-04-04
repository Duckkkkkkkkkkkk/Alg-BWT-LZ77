import pickle

def compute_suffix_array(input_text):
    len_text = len(input_text)
    suff = [(i, input_text[i:]) for i in range(len_text)]
    suff.sort(key=lambda x: x[1])
    suffix_arr = [i for i, _ in suff]
    return suffix_arr


def find_last_char(input_text, suffix_arr):
    n = len(suffix_arr)
    bwt_arr = ""
    for i in range(n):
        j = suffix_arr[i] - 1
        if j < 0:
            j = j + n
        bwt_arr += input_text[j]
    return bwt_arr


def BWT_encode(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        input_text = file.read().strip()

    input_text += '$'

    suffix_arr = compute_suffix_array(input_text)
    bwt_arr = find_last_char(input_text, suffix_arr)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(bwt_arr)

    original_length_bits = len(input_text) * 8  # Assuming 8 bits per character

    encoded_length_bits = len(bwt_arr.encode('utf-8')) * 8

    print(f"Длина исходного текста: {original_length_bits} бит")
    # print(f"Длина текста, закодированного алгоритмом Барроуза-Уиллера: {encoded_length_bits} бит")


def longest_prefix_from(Left, Right):
    LongestPrefixLength = 0
    LongestPrefixPos = -1

    while 1:
        PrefixLength = LongestPrefixLength + 1
        if PrefixLength >= len(Right):
            break

        Prefix = Right[0: PrefixLength]
        PrefixPos = Left.find(Prefix)

        if PrefixPos == -1:
            break

        LongestPrefixLength = PrefixLength
        LongestPrefixPos = PrefixPos
    return (LongestPrefixLength, LongestPrefixPos)


def codeBufferLZ77(Buffer):
    Result = []
    CodePos = 0

    while CodePos < len(Buffer):
        Left = Buffer[0:CodePos]
        Right = Buffer[CodePos:]

        (PrefixLength, PrefixPos) = longest_prefix_from(Left, Right)

        if (PrefixLength == 0):
            # Each tuple: 32 bits (offset) + 32 bits (length) + 8 bits (character)
            Result.append((0, 0, Buffer[CodePos]))
            CodePos = CodePos + 1
        else:
            # Each tuple: 32 bits (offset) + 32 bits (length) + 8 bits (character)
            Result.append((CodePos - PrefixPos, PrefixLength, Buffer[CodePos + PrefixLength]))
            CodePos = CodePos + PrefixLength + 1  # Move to the next character after the matched substring
    return Result


def LZ77_encode(input_filename, output_filename, window_size):
    input_file = open(input_filename, 'r', encoding='utf-8')

    coded_text = []
    while 1:
        buffer = input_file.read(window_size)
        if buffer == '':
            break
        code = codeBufferLZ77(buffer)
        coded_text += code

    input_file.close()

    with open(output_filename, 'wb') as output_file:
        pickle.dump(coded_text, output_file)

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        for item in coded_text:
            output_file.write(str(item) + '\n')

    encoded_text_size_bits = len(coded_text) * 8  # Each tuple is 32 + 32 + 8 bits

    # print(f"Длина текста, закодированного алгоритмом LZ77: {encoded_text_size_bits} бит")
    print(f"Длина закодированного текста: {encoded_text_size_bits} бит")


if __name__ == "__main__":
    input_file = 'C:/Users/Анастасия/Desktop/3 course/codingTheory/ArchivatorLab1/mumu2.txt'
    output_file = 'C:/Users/Анастасия/Desktop/3 course/codingTheory/ArchivatorLab1/mumu_encoding.txt'

    BWT_encode(input_file, output_file)
    LZ77_encode('C:/Users/Анастасия/Desktop/3 course/codingTheory/ArchivatorLab1/mumu_encoding.txt',
                'C:/Users/Анастасия/Desktop/3 course/codingTheory/ArchivatorLab1/mumu_encoding.txt',
                100)
    print("Кодированный текст был записан в файл", output_file)
