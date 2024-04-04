import sys

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

    return decoded_str  # Return the decoded string

def decode_and_write(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        bwt_arr = file.read().strip()

    decoded_str = invert(bwt_arr)

    # Calculate and print the length of the decoded text in bits
    decoded_length_bits = len(decoded_str) * 8  # Assuming 8 bits per character
    print(f"Length of decoded text: {decoded_length_bits} bits")

    # Remove the '$' symbol before writing to the output file
    decoded_str_without_marker = decoded_str.replace('$', '')

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(decoded_str_without_marker[::-1])

    print("Burrows-Wheeler Transform has been decoded and written to", output_file)

if __name__ == "__main__":
    input_file = 'C:/Users/Анастасия/Desktop/3 course/codingTheory/ArchivatorLab1/mumu_decoding_LZ77.txt'
    output_file = 'C:/Users/Анастасия/Desktop/3 course/codingTheory/ArchivatorLab1/mumu_decoding_BWT.txt'

    decode_and_write(input_file, output_file)
