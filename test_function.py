from function import display_cost, validate_weight
import pytest

@pytest.mark.code # pytest -m code
def test_1kg_input_1():
    input = 1
    expected_result = 32
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.code # pytest -m code
def test_10kg_input_10():
    input = 10
    expected_result = 320
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.code # pytest -m code
def test_50kg_input_50():
    input = 50
    expected_result = 1600
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.code # pytest -m code
def test_100kg_input_100():
    input = 100
    expected_result = 3200
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.code # pytest -m code
def test_500kg_input_500():
    input = 500
    expected_result = 16000
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.code # pytest -m code
def test_1000kg_input_1000():
    input = 1000
    expected_result = 32000
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.code # pytest -m code
def test_1500kg_input_1500():
    input = 1500
    expected_result = 48000
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.code # pytest -m code
def test_2000kg_input_2000():
    input = 2000
    expected_result = 64000
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.code # pytest -m code
def test_2500kg_input_2500():
    input = 2500
    expected_result = 80000
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.code # pytest -m code
def test_3000kg_input_3000():
    input = 3000
    expected_result = 96000
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_0():
    input = 0
    expected_result = "out of range"
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_3001():
    input = 3001
    expected_result = "out of range"
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_minus_10():
    input = -10
    expected_result = "out of range"
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_3500():
    input = 3500
    expected_result = "out of range"
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_input_integer_input_1_1():
    input = 1.1
    expected_result = "input integer"
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_input_integer_input_char_a():
    input = "a"
    expected_result = "input integer"
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_input_integer_input_char_sharp():
    input = "#"
    expected_result = "input integer"
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_0_5():
    input = 0.5
    expected_result = "out of range"
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_out_of_range_input_minus_1_5():
    input = -10.5
    expected_result = "out of range"
    actual_result = display_cost(input)
    assert expected_result == actual_result

@pytest.mark.validate # pytest -m validate
def test_input_integer_input_1_5():
    input = 1.5
    expected_result = "input integer"
    actual_result = display_cost(input)
    assert expected_result == actual_result