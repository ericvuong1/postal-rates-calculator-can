import sys
import csv

#main method that will run the post rate calculator. argc is the parameters count and argv contains the parameters
def main(argc, argv):

    #CHECK CORRECT NUMBER OF ARGUMENTS
    if (argc < 7 or argc > 7):
        display_text = "Usage: starting_code ending_code length width height weight post_type"
        return display_text     #terminate with error display string

    #CHECK VALID POSTAL CODES
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

    #CHECK VALID LENGTH
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

    #CHECK VALID WIDTH
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

    #CHECK VALID HEIGHT
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

    #CHECK VALID WEIGHT
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

    #CHECK VALID POST TYPE
    post_type = argv[6]

    if post_type != "Regular" and post_type != "Xpress" and post_type != "Priority":
        display_text = "Error: not a valid post type (Regular, Xpress or Priority) case sensitive."
        return display_text

    #CALCULATE TOTAL POST RATE
    total_cost = "{0:.2f}".format(calcVolumePrice(length,width,height) + calcWeightPrice(weight) + calcPostTypePrice(post_type))
    print(total_cost)
    return total_cost


#function to calculate the volume price (assumed to be 5 dollars per meters cube)
def calcVolumePrice(length, width, height):
    price = (0.01 * length * 0.01 * width * 0.01 * height) * 5
    return price


#function to calculate the weight price (assumed to be 50 cents per kilogram)
def calcWeightPrice(weight):
    price = 0.5 * weight
    return price


#function to return the correct price of the post type (assumed to be 5 for regular, 10 for xpress, 15 for priority)
def calcPostTypePrice(post_type):
    if post_type == "Regular":
        return 5.00
    elif post_type == "Xpress":
        return 10.00
    elif post_type == "Priority":
        return 15.00

#This is to test or run the program
main(7, ["h4k2g2", "v9g8r7", "132", "14", "25.1", "15.6", "Priority"])
