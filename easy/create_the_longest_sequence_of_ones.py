# TODO Given some bitstring b, you may change one bit from a 0 to a 1 in order to create
#  the longest possible sequence of consecutive 1s. Output the length of the resulting longest sequence.

def length_of_the_longest_sequence_in_bitstring(text):
    temp_result = text.split('0')
    max_sequence, temp_sum, last_element = 0, 0, 0
    for entry in temp_result:
        temp_sum = len(entry) + last_element + 1
        max_sequence = max(max_sequence, temp_sum)
        last_element = len(entry)
    return max_sequence


if __name__ == '__main__':
    bitstring = input()
    print(length_of_the_longest_sequence_in_bitstring(bitstring))
