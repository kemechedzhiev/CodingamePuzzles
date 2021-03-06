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
    # TODO fix that func!
    global rotors
    result = ''
    for i, letter in enumerate(message_to_decode):
        new_letter = letter
        for rotor in reversed(rotors):
            new_letter = change_letters(new_letter, rotor)
        caesar_rotor = generate_abc_shifted(shift_num + i)
        new_letter = change_letters(new_letter, caesar_rotor)
        result += new_letter
    return result


def generate_abc_shifted(abc_shift):
    global rotors
    abc = sorted(rotors[0])
    if abc_shift > len(abc):
        abc_shift %= len(abc)
    return abc[abc_shift:] + abc[:abc_shift]


def change_letters(letter, rotor):
    abc = sorted(rotor)
    index = abc.index(letter)
    return rotor[index]


if __name__ == '__main__':
    task = input()
    shift = int(input())
    rotors = [input() for _ in range(3)]
    message = input()
    operation = {'ENCODE': encode, 'DECODE': decode}
    print(operation[task](shift, message))

# DECODE
# 9
# BDFHJLCPRTXVZNYEIWGAKMUSQO
# AJDKSIRUXBLHWTMCQGZNPYFVOE
# EKMFLGDQVZNTOWYHXUSPAIBRCJ
# PQSACVVTOISXFXCIAMQEM
