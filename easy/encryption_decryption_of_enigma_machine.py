# TODO During World War II, the Germans were using an encryption code called Enigma – which
#  was basically an encryption machine that encrypted messages for transmission. The Enigma code
#  went many years unbroken. Here's How the basic machine works:
#  First Caesar shift is applied using an incrementing number:
#  If String is AAA and starting number is 4 then output will be EFG.
#  A + 4 = E
#  A + 4 + 1 = F
#  A + 4 + 1 + 1 = G
#  Now map EFG to first ROTOR such as:
#  ABCDEFGHIJKLMNOPQRSTUVWXYZ
#  BDFHJLCPRTXVZNYEIWGAKMUSQO
#  So EFG becomes JLC. Then it is passed through 2 more rotors to get the final value.
#  If the second ROTOR is AJDKSIRUXBLHWTMCQGZNPYFVOE, we apply the substitution step again thus:
#  ABCDEFGHIJKLMNOPQRSTUVWXYZ
#  AJDKSIRUXBLHWTMCQGZNPYFVOE
#  So JLC becomes BHD.
#  If the third ROTOR is EKMFLGDQVZNTOWYHXUSPAIBRCJ, then the final substitution is:
#  ABCDEFGHIJKLMNOPQRSTUVWXYZ
#  EKMFLGDQVZNTOWYHXUSPAIBRCJ
#  So BHD becomes KQF.
#  Final output is sent via Radio Transmitter.
# Input
# Line 1: ENCODE or DECODE
# Line 2: Starting shift N
# Lines 3-5:
# BDFHJLCPRTXVZNYEIWGAKMUSQO ROTOR I
# AJDKSIRUXBLHWTMCQGZNPYFVOE ROTOR II
# EKMFLGDQVZNTOWYHXUSPAIBRCJ ROTOR III
# Line 6: Message to Encode or Decode
# Output
# Encoded or Decoded String
ABC_LENGTH = 26
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encode(shift_num, message_to_encode):
    global rotors
    result = ''
    for i, letter in enumerate(message_to_encode):
        caesar_rotor = generate_abc_shifted(shift_num + i)
        new_letter = letter
        for rotor in [caesar_rotor, *rotors]:
            new_letter = change_letters(new_letter, rotor)
        result += new_letter
    return result


def decode(shift_num, message_to_decode):
    global rotors
    result = ''
    for i, letter in enumerate(message_to_decode):
        new_letter = letter
        caesar_rotor = generate_abc_shifted(shift_num + i)
        for rotor in [*reversed(rotors), caesar_rotor]:
            # print(rotor)
            new_letter = reverse_change_letters(new_letter, rotor)
        result += new_letter
        # exit(0)
    return result


def generate_abc_shifted(abc_shift):
    global rotors
    if abc_shift < 0:
        abc_shift += ABC_LENGTH
    if abc_shift > ABC_LENGTH:
        abc_shift %= ABC_LENGTH
    return ABC[abc_shift:] + ABC[:abc_shift]


def change_letters(letter, rotor):
    index = ABC.index(letter)
    return rotor[index]


def reverse_change_letters(letter, rotor):
    index = rotor.index(letter)
    return ABC[index]


if __name__ == '__main__':
    task = input()
    shift = int(input())
    rotors = [input() for _ in range(3)]
    message = input()
    operation = {'ENCODE': encode, 'DECODE': decode}
    print(operation[task](shift, message.upper()))

