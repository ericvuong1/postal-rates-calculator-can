import pytest
import postal_calc


def test_no_args():
    parameter_count = 0
    parameters = ""
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Usage: starting_code ending_code length width height weight post_type"


def test_args_less7():
    parameter_count = 3
    parameters = "h4k2g2 h1t3r3 3"
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Usage: starting_code ending_code length width height weight post_type"


def test_args_more7():
    parameter_count = 8
    parameters = "h4k2g2 h3l1o0 1 2 3 4 Xpress"
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Usage: starting_code ending_code length width height weight post_type"


def test_invalid_startcode():
    parameter_count = 7
    parameters = "123456 654321 1 2 3 4 Xpress"
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Error: not a valid canadian starting postal code."
















# def test_1():
#     parameter_count = 0
#     parameters = ""
#     return_rate = postal_calc.main(parameter_count, parameters)
#     assert return_rate == "ZERO ARGUMENT!!!"
#
# def test_no():
#     parameter_count = 6
#     parameters = "h4k2g2 h4k2g2 3 4 5 8"
#     return_rate = postal_calc.main(parameter_count, parameters)
#     assert return_rate == "Usage: ENTER"
