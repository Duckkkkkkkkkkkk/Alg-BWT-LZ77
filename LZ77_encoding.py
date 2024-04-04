import pickle
import os

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

def lz77encode(input_filename, output_filename, window_size):
    input_file = open(input_filename, 'r', encoding='utf-8')

    coded_text = []
    while 1:
        buffer = input_file.read(window_size)
        if buffer == '':
            break
        code = codeBufferLZ77(buffer)
        coded_text += code

    input_file.close()

    # Write encoded text using pickle with 'wb' mode
    with open(output_filename, 'wb') as output_file:
        pickle.dump(coded_text, output_file)

    # Open the file again in 'w' mode and write each element with utf-8 encoding
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        for item in coded_text:
            output_file.write(str(item) + '\n')

    with open(input_filename, 'r', encoding='utf-8') as input_file:
        original_text = input_file.read()
    original_text_size_bits = len(original_text) * 8
    print(f"Original Text Size (bits): {original_text_size_bits}")

    encoded_text_size_bits = len(coded_text) * 8

    print(f"Encoded Text Size (bits): {encoded_text_size_bits}")

if __name__ == "__main__":
    lz77encode('C:/Users/Анастасия/Desktop/3 course/codingTheory/ArchivatorLab1/mumu_encoding_BWT.txt', 'C:/Users/Анастасия/Desktop/3 course/codingTheory/ArchivatorLab1/mumu_encoding_LZ77.txt', 100)
