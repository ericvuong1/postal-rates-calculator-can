import csv
import math

# load csv file
with open('postal-code-generator.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    codes = []
    longitudes = []
    latitudes = []

    for row in readCSV:
        code = row[0]
        longitude = row[1]
        latitude = row[2]

        codes.append(code)
        longitudes.append(longitude)
        latitudes.append(latitude)


# cost settings
cost_per_distance_multiple = 5
distance_multiple = 100
cost_per_kg = 1.20
regular_shipping_cost = 5.00
xpress_shipping_cost = 10.00
priority_shipping_cost = 15.00
cost_per_m_cubed = 5

def get_postal_position():
    """input a valid canadian postal code
    return a list (longitude, latitude)"""
    while True:
        try:
            what_code = input('Please enter a valid postal code: ').lower()
            if what_code in codes:
                codex = codes.index(what_code)
                retrieved_code = codes[codex]
                retrieved_longitude = longitudes[codex]
                retrieved_latitude = latitudes[codex]
                print(
                    'Entered postal code: ' + retrieved_code + ' is\nLongitude: ' + retrieved_longitude
                    + '\nLatitude: ' + retrieved_latitude)
                return int(retrieved_longitude), int(retrieved_latitude)
            else:
                print('Postal code not found, or is not a valid canadian postal code.')
                continue
        except Exception as e:
            print(e)


def calculate_distance(start, destination):
    return math.ceil(math.sqrt((destination[0] - start[0]) ** 2 + (destination[1] - start[1]) ** 2))


def calculate_volume():
    while True:
        print("Please enter the dimensions of the item to ship. Please note that the dimensions cannot exceed 2 m.")
        try:
            height = float(input("Enter height in cm: "))
            if height <= 0 or height > 200:
                print("You didn't enter a non negative height or exceeded the dimensions, please try again.")
                continue
            length = float(input("Enter length in cm: "))
            if length <= 0 or length >= 200:
                print("You didn't enter a non negative length or exceeded the dimensions, please try again.")
                continue
            width = float(input("Enter width in cm: "))
            if width <= 0 or width >= 200:
                print("You didn't enter a non negative width or exceeded the dimensions, please try again.")
                continue
            return "{0:.3f}".format(height/100.0 * width/100.0 * length/100.0)
        except ValueError as e:
            print("You didn't enter a number, please try again.")


def calculate_weight_price():
    while True:
        print("Please enter the weight of the item to ship. Please note that the weight cannot exceed 10 kg")
        try:
            weight_input = float(input("Enter weight in kg: "))
            if weight_input <= 0 or weight_input > 10:
                print("You didn't enter a non negative weight or you exceeded the weight limit, please try again")
                continue
            return weight_input * cost_per_kg, weight_input
        except ValueError as e:
            print("You didn't enter a number, please try again")


def choose_post_type():
    while True:
        post_type = input("Please choose the post type: Regular ($5), Xpress (10$) or Priority (15$)").lower()
        accepted_strings = {'regular', 'xpress', 'priority'}
        if post_type not in accepted_strings:
            print("Please enter any of the available post type")
            continue
        elif post_type == 'regular':
            return post_type, regular_shipping_cost
        elif post_type == 'xpress':
            return post_type, xpress_shipping_cost
        elif post_type == 'priority':
            return post_type, priority_shipping_cost