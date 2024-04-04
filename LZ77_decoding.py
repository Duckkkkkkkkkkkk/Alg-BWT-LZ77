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
    # Read the encoded text from the file
    with open(input_file, 'r', encoding='utf-8') as file:
        encoded_text = file.readlines()

    # Decode the text using the LZ77 algorithm
    decoded_text = decodeLZ77(encoded_text)

    # Calculate the length of the original text in bits
    original_text_length = len(decoded_text) * 8
    print(f"Original Text Size (bits): {original_text_length}")

    # Write the decoded text to a new file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(decoded_text)

if __name__ == "__main__":
    input_file = 'C:/Users/Анастасия/Desktop/3 course/codingTheory/ArchivatorLab1/mumu_encoding_LZ77.txt'
    output_file = 'C:/Users/Анастасия/Desktop/3 course/codingTheory/ArchivatorLab1/mumu_decoding_LZ77.txt'
    main(input_file, output_file)
