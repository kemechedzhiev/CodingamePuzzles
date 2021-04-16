# TODO Given a fixed set of characters, a code is a table that gives the encoding to use for each character.
#  A prefix code is a code with the prefix property, which is that there is no character with an encoding
#  that is a prefix (initial segment) of the encoding of another character. Your goal is to decode an encoded string
#  using the given prefix code, or say that is not possible.
#  Example of encoding.
#  Given the string "abracadabra" and the prefix code:
#  a -> 1
#  b -> 001
#  c -> 011
#  d -> 010
#  r -> 000
#  The resulting encoding is: 10010001011101010010001
#  Thus, if your are given the code above and the input 10010001011101010010001, you should output the string
#  "abracadabra".
#  With the same prefix code, if the input is 0000, then you should tell that there is an error at index 3.
#  Indeed, the first three characters of this input can be decoded to give an 'r', but that leaves 0,
#  which cannot be decoded.
#  INPUT
#  Line 1: A single integer N representing the number of association in the prefix-code table.
#  Next N lines: A binary code Bi and an integer Ci, which tells that the character with ASCII code Ci
#  will be encoded by Bi.
#  Next line: The binary code S of an encoded string.
#   OUTPUT
#  - If it is not possible to decode the encoded string, print DECODE FAIL AT INDEX i with i the first index
#  in the encoded string where the decoding fails (index starts from 0).
#  - Otherwise print the decoded string.


def decode_with_prefix(prefix_table, string_to_decode):
    if len(prefix_table) == 0:
        return 'DECODE FAIL AT INDEX 0'
    text_buffer = ''
    result_string = ''
    max_len = max([len(elem) for elem in prefix_table.keys()])
    for index, symbol in enumerate(string_to_decode):
        text_buffer += symbol
        if text_buffer in prefix_table.keys():
            result_string += prefix_table[text_buffer]
            text_buffer = ''
            continue
        if len(text_buffer) > max_len or index == len(string_to_decode) - 1:
            return f'DECODE FAIL AT INDEX {index - len(text_buffer) + 1}'
    return result_string


if __name__ == '__main__':
    size_of_dict = int(input())
    alphabet = dict()
    for _ in range(size_of_dict):
        row = [i for i in input().split()]
        alphabet[row[0]] = chr(int(row[1]))
    text_to_decode = input()
    print(decode_with_prefix(alphabet, text_to_decode))
