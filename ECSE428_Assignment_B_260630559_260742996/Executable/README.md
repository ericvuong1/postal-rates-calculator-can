# postal-rates-calculator-can
Postal rates calculator for Canada.
ECSE 428 - Assignment B - Test Driven Development

Running the file:

Note that this is developed in Python, which is a scripting language.
Thus, executing this application needs to have python 3.6 installed like
running any other scripts on a command line. The aforementioned .csv file must
be in the same directory as the script. The sha-bang is #!/usr/bin/env python3.6

for e.g.:

valid input:
./postal_calc.py h4k2g2 h4k2g2 100 100 100 1 Xpress

valid output:
The total cost is: 15.50

invalid input:
./postal_calc.py h4k2g2 l3m0j2 100 100 100 1 Xpress dd

invalid output:
Usage: starting_code ending_code length width height weight post_type
