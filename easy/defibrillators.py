import math
# TODO The input data you require for your program is provided in text format.
#  This data is comprised of lines, each of which represents a defibrillator. Each defibrillator
#  is represented by the following fields:
#  A number identifying the defibrillator
#  Name
#  Address
#  Contact Phone number
#  longitude (degrees)
#  Latitude (degrees)
#  These fields are separated by a semicolon (;).
#  Beware: the decimal numbers use the comma (,) as decimal separator. Remember to turn the comma (,)
#  into dot (.) if necessary in order to use the data in your program.
#  DISTANCE
#  The distance d between two points A and B will be calculated using the following formula:
#  x = (longitudeB - longitudeA) * cos((latitudeA + latitudeB)/2)
#  y = (latitudeB - latitudeA)
#  d = sqrt(x^2 + y^2) * 6371
#  In this formula, the latitudes and longitudes are expressed in radians. 6371 corresponds to
#  the radius of the earth in km.
#  The program will display the name of the defibrillator located the closest to the user’s position.
#  This position is given as input to the program.
#  INPUT
#  Line 1: User's longitude (in degrees)
#  Line 2: User's latitude (in degrees)
#  Line 3: The number N of defibrillators located in the streets of Montpellier
#  N next lines: a description of each defibrillator
#  OUTPUT
#  The name of the defibrillator located the closest to the user’s position.
# Example
# Input
# 3,879483
# 43,608177
# 3
# 1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;;3,87952263361082;43,6071285339217
# 2;Hotel de Ville;1 place Georges Freche 34267 Montpellier;;3,89652239197876;43,5987299452849
# 3;Zoo de Lunaret;50 avenue Agropolis 34090 Mtp;;3,87388031141133;43,6395872778854
# Output
# Maison de la Prevention Sante


def print_nearest_defibrillator_address(current_longitude, current_latitude, defibrillators_addresses):
    minimum_distance = 10000
    nearest_defibrillator = 'hospital'
    for i in defibrillators_addresses.keys():
        defibrillator_coordinates = defibrillators_addresses[i]
        def_coordinates = defibrillator_coordinates.split(';')
        defibrillator_longitude = float(def_coordinates[0].replace(',', '.'))
        defibrillator_latitude = float(def_coordinates[1].replace(',', '.'))
        x = (defibrillator_longitude - current_longitude) * math.pi/180 * \
            math.cos((current_latitude + defibrillator_latitude) / 2 * math.pi/180)
        y = (defibrillator_latitude - current_latitude) * math.pi / 180
        d = math.sqrt(x * x + y * y) * 6371
        if d < minimum_distance:
            minimum_distance = d
            nearest_defibrillator = i
    print(nearest_defibrillator)
    return 0


if __name__ == '__main__':
    # print('Mission started')
    user_longitude_raw = input()
    user_longitude = float(user_longitude_raw.replace(',', '.'))
    user_latitude_raw = input()
    user_latitude = float(user_latitude_raw.replace(',', '.'))
    quantity = int(input())
    defibrillators = dict()
    for i in range(quantity):
        raw_string = input()
        raw_string_to_list = raw_string.split(';;')
        defibrillators[raw_string_to_list[0].split(';')[1]] = raw_string_to_list[1]
    print_nearest_defibrillator_address(user_longitude, user_latitude, defibrillators)
