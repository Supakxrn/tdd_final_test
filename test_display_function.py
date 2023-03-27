from function import display_cost
import pytest

@pytest.mark.display # pytest -m display
@pytest.mark.parametrize('input_weight ,expected_result', [
    (1,32), (10,320), (50,1600), (100,3200), (500,16000), (1000,32000), (1500,48000), (2000,64000), (2500,80000), (3000,96000), (0,"out of range"), (3001,"out of range"), 
    (-10,"out of range"), (3500,"out of range"), (1.1,"input integer"), ("a","input integer"), ("#","input integer"),(0.5,"out of range"), (-10.5,"out of range"), 
    (1.5,"input integer")
])
def test_display(input_weight, expected_result):
    actual_result = display_cost(input_weight)
    assert expected_result == actual_result