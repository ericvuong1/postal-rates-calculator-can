import helper
import pytest
import sys
import postal_calc


# def test_no_args(capsys):
#     #postal_calc.
#     out, err = capsys.readouterr()
#     assert out == "Usage: ENTER\n"
#
# def test_no_args123(capsys):
#     postal_calc.printMessage()
#     out, err = capsys.readouterr()
#     assert out == "Usage: Please enter a valid canadian postal code\n"

# def test_get_input_less_7args(capsys):
#     # postal_calc.getInput()
#     out, err = capsys.readouterr()


def test_1():
    parameter_count = 0
    parameters = ""
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "ZERO ARGUMENT!!!"

def test_no():
    parameter_count = 6
    parameters = "h4k2g2 h4k2g2 3 4 5 8"
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Usage: ENTER"
