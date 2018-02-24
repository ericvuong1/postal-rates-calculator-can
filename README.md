# postal-rates-calculator-can
Postal rates calculator for Canada.
ECSE 428 - Assignment B - Test Driven Development

Assumption:

A valid postal code must be entered, and is verified with an existing look-up table.
Each postal code will contain an approximate longitude and latitude, which will be thought as position x and y for simplicity.

For e.g.

Postal Code: H4K 2G2	Position X: 100		Position Y: 150
Postal Code: H9J 2P7	Position X: -50		Position Y: 213

A Base price will be calculated according using the distance formula and the Pythagorean Theorem.

e.g. Start: H4K 2G2, End: H9J 2P7
	Distance calculated: SQRT((213-150)^2+(-50-100)^2)
Base price will increase at multiples of $5.00 / 100km starting at a base price of $5.00.

