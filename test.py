import pytest
import postal_calc


def test_no_args():
    parameter_count = 0
    parameters = []
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Usage: starting_code ending_code length width height weight post_type"


def test_args_less7():
    parameter_count = 3
    parameters = ["postal_calc.py" "h4k2g2" "h1t3r3" "3"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Usage: starting_code ending_code length width height weight post_type"


def test_args_more7():
    parameter_count = 8
    parameters = ["postal_calc.py" "h4k2g2" "h3l1o0" "1" "2" "3" "4" "Xpress" "4"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Usage: starting_code ending_code length width height weight post_type"


def test_invalid_startcode():
    parameter_count = 7
    parameters = ["postal_calc.py" "123456", "654321", "1", "2", "3", "4", "Xpress"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Error: not a valid canadian starting postal code."


def test_invalid_destinationcode():
    parameter_count = 7
    parameters = ["postal_calc.py" "h4k2g2", "654321", "1", "2", "3", "4", "Xpress"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Error: not a valid canadian destination postal code."


def test_invalid_length_format():
    parameter_count = 7
    parameters = ["postal_calc.py" "h4k2g2", "v9g8r7", "abc", "2", "3", "4", "Xpress"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Error: not a valid numerical length (cm)."


def test_length_less10():
    parameter_count = 7
    parameters = ["postal_calc.py" "h4k2g2", "v9g8r7", "-5", "2", "3", "4", "Xpress"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Error: length must be at least 10cm."


def test_length_more200():
    parameter_count = 7
    parameters = ["postal_calc.py" "h4k2g2", "v9g8r7", "244", "2", "3", "4", "Xpress"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Error: maximum length is 200cm."


def test_invalid_width_format():
    parameter_count = 7
    parameters = ["postal_calc.py" "h4k2g2", "v9g8r7", "50", "abc", "3", "4", "Xpress"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Error: not a valid numerical width (cm)."


def test_width_less10():
    parameter_count = 7
    parameters = ["postal_calc.py" "h4k2g2", "v9g8r7", "50", "2", "3", "4", "Xpress"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Error: width must be at least 10cm."


def test_width_more200():
    parameter_count = 7
    parameters = ["postal_calc.py" "h4k2g2", "v9g8r7", "50", "201", "3", "4", "Xpress"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Error: maximum width is 200cm."


def test_invalid_height_format():
    parameter_count = 7
    parameters = ["postal_calc.py" "h4k2g2", "v9g8r7", "50", "50", "abc", "4", "Xpress"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Error: not a valid numerical height (cm)."


def test_height_less10():
    parameter_count = 7
    parameters = ["postal_calc.py" "h4k2g2", "v9g8r7", "50", "50", "0", "4", "Xpress"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Error: height must be at least 10cm."


def test_height_more200():
    parameter_count = 7
    parameters = ["postal_calc.py" "h4k2g2", "v9g8r7", "50", "50", "400", "4", "Xpress"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Error: maximum height is 200cm."


def test_volume_price():
    length = 100
    width = 100
    height = 100
    price = postal_calc.calcVolumePrice(length, width, height)
    assert price == 5.00


def test_invalid_weight_format():
    parameter_count = 7
    parameters = ["postal_calc.py" "h4k2g2", "v9g8r7", "50", "50", "50", "abc", "Xpress"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Error: not a valid numerical weight (kg)."


def test_weight_less_minimum():
    parameter_count = 7
    parameters = ["postal_calc.py" "h4k2g2", "v9g8r7", "50", "50", "50", "0", "Xpress"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Error: minimum weight is 0.1kg."


def test_weight_more_maximum():
    parameter_count = 7
    parameters = ["postal_calc.py" "h4k2g2", "v9g8r7", "50", "50", "50", "31", "Xpress"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Error: maximum weight is 30kg."


def test_weight_price():
    weight = 3
    price = postal_calc.calcWeightPrice(weight)
    assert price == 1.5


def test_invalid_post_type():
    parameter_count = 7
    parameters = ["postal_calc.py" "h4k2g2", "v9g8r7", "100", "100", "100", "1", "hello"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "Error: not a valid post type (Regular, Xpress or Priority) case sensitive."


def test_regular_type_price():
    post_type = "Regular"
    price = postal_calc.calcPostTypePrice(post_type)
    assert price == 5.00


def test_Xpress_type_price():
    post_type = "Xpress"
    price = postal_calc.calcPostTypePrice(post_type)
    assert price == 10.00


def test_priority_type_price():
    post_type = "Priority"
    price = postal_calc.calcPostTypePrice(post_type)
    assert price == 15.00


def test_total_post_rate_cost():
    parameter_count = 7
    parameters = ["postal_calc.py" "h4k2g2", "v9g8r7", "100", "100", "100", "1", "Xpress"]
    return_rate = postal_calc.main(parameter_count, parameters)
    assert return_rate == "15.50"