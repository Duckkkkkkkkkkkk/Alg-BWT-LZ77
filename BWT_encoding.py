import sys

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

def encode_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        input_text = file.read().strip()

    input_text += '$'

    suffix_arr = compute_suffix_array(input_text)
    bwt_arr = find_last_char(input_text, suffix_arr)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(bwt_arr)

    # Calculate and print the length of the original and encoded texts in bits
    original_length_bits = len(input_text) * 8  # Assuming 8 bits per character

    # Using utf-8 encoding to get the byte representation
    encoded_length_bits = len(bwt_arr.encode('utf-8')) * 8

    print(f"Length of original text: {original_length_bits} bits")
    print(f"Length of encoded text: {encoded_length_bits} bits")

    print("Encoded text has been written to", output_file)

if __name__ == "__main__":
    input_file = 'C:/Users/Анастасия/Desktop/3 course/codingTheory/ArchivatorLab1/mumu2.txt'
    output_file = 'C:/Users/Анастасия/Desktop/3 course/codingTheory/ArchivatorLab1/mumu_encoding_BWT.txt'

    encode_text(input_file, output_file)
