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



















