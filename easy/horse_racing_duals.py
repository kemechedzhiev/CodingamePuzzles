# TODO Casablanca’s hippodrome is organizing a new type of horse racing: duals. During a dual, only two horses
#  will participate in the race. In order for the race to be interesting, it is necessary to try to select
#  two horses with similar strength.
#  Write a program which, using a given number of strengths, identifies the two closest strengths
#  and shows their difference with an integer (≥ 0).
#  INPUT
#  Line 1: Number N of horses
#  The N following lines: the strength Pi of each horse. Pi is an integer.
#  OUTPUT
#  The difference D between the two closest strengths. D is an integer greater than or equal to 0.


def check_the_difference(number_of_cases):
    dataset = [int(input()) for i in range(number_of_cases)]
    difference = 10000
    previous_entry = 0
    for entry in sorted(dataset):
        if abs(entry - previous_entry) <= difference:
            difference = abs(entry - previous_entry)
        previous_entry = entry
    return difference


if __name__ == '__main__':
    num_of_horses = int(input())
    print(f'{check_the_difference(num_of_horses)}')

