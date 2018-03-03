import helper
import pytest
import sys
import postal_calc


def test_no_args(capsys):
    postal_calc.
    out, err = capsys.readouterr()
    assert out == "Usage: ENTER\n"

def test_no_args123(capsys):
    postal_calc.printMessage()
    out, err = capsys.readouterr()
    assert out == "Usage: Please enter a valid canadian postal code\n"

# def test_get_input_less_7args(capsys):
#     # postal_calc.getInput()
#     out, err = capsys.readouterr()

