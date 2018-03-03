import sys
import csv


def main(argc, argv):

    if (argc < 7 or argc > 7):
        display_text = "Usage: starting_code ending_code length width height weight post_type"
        return display_text

    with open('postal-code-generator.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        codes = []

        for row in readCSV:
            code = row[0]
            codes.append(code)

    if argv[0] not in codes:
        display_text = "Error: not a valid canadian starting postal code."
        return display_text

    if argv[1] not in codes:
        display_text = "Error: not a valid canadian destination postal code."
        return display_text

    try:
        length = float(argv[2])
    except:
        display_text = "Error: not a valid numerical length (cm)."
        return display_text

    if length < 10:
        display_text = "Error: length must be at least 10cm."
        return display_text

    if length > 200:
        display_text = "Error: maximum length is 200cm."
        return display_text

    try:
        width = float(argv[3])
    except:
        display_text = "Error: not a valid numerical width (cm)."
        return display_text

    if width < 10:
        display_text = "Error: width must be at least 10cm."
        return display_text

    if width > 200:
        display_text = "Error: maximum width is 200cm."
        return display_text

    try:
        height = float(argv[4])

    except:
        display_text = "Error: not a valid numerical height (cm)."
        return display_text

    if height < 10:
        display_text = "Error: height must be at least 10cm."
        return display_text

    if height > 200:
        display_text = "Error: maximum height is 200cm."
        return display_text

    try:
        weight = float(argv[5])
    except:
        display_text = "Error: not a valid numerical weight (kg)."
        return display_text

    if weight < 0.1:
        display_text = "Error: minimum weight is 0.1kg."
        return display_text

    if weight > 30:
        display_text = "Error: maximum weight is 30kg."
        return display_text

    post_type = argv[6]

    if post_type != "Regular" and post_type != "Xpress" and post_type != "Priority":
        display_text = "Error: not a valid post type (Regular, Xpress or Priority) case sensitive."
        return display_text

    total_cost = "{0:.2f}".format(calcVolumePrice(length,width,height) + calcWeightPrice(weight) + calcPostTypePrice(post_type))

    return total_cost


def calcVolumePrice(length, width, height):
    price = (0.01 * length * 0.01 * width * 0.01 * height) * 5
    return price


def calcWeightPrice(weight):
    price = 0.5 * weight
    return price


def calcPostTypePrice(post_type):
    if post_type == "Regular":
        return 5.00
    elif post_type == "Xpress":
        return 10.00
    elif post_type == "Priority":
        return 15.00





