import string
# TODO Print the string in ASCII style
#  Input:
#  Line 1: the width L of a letter represented in ASCII art. All letters are the same width.
#  Line 2: the height H of a letter represented in ASCII art. All letters are the same height.
#  Line 3: The line of text T, composed of N ASCII characters.
#  Following lines: the string of characters ABCDEFGHIJKLMNOPQRSTUVWXYZ? Represented in ASCII art.
#  Output:
#  The text T in ASCII art.
#  The characters a to z are shown in ASCII art by their equivalent in upper case.
#  The characters that are not in the intervals [a-z] or [A-Z] will be shown as a question mark in ASCII art.


length = int(input())
height = int(input())
text = input()
alphabet = ''
for i in range(height):
    alphabet += input()


def get_letter_position(needed_letter):
    if needed_letter.isalpha():
        letter_index = string.ascii_letters.index(needed_letter) - 26
        letter_position = (27 * length * i) + (letter_index * length)
        return letter_position
    else:
        letter_index = 26
        letter_position = (27 * length * i) + (letter_index * length)
        return letter_position


for i in range(height):
    for letter in text:
        position = get_letter_position(letter.upper())
        print(f"{alphabet[position: position + length]}", end='')
    print("")
