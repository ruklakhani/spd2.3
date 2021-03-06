# test_one.py
import math 
import pytest
from exercise2 import get_age_carbon_14_dating
from exercise3 import calculate_stat
from exercise4 import extract_position 

def test_get_age_carbon_14_dating():
    
    assert math.isclose(get_age_carbon_14_dating(0.35), 8680.34, rel_tol=.01)
    assert get_age_carbon_14_dating(0) is None
    assert get_age_carbon_14_dating(1) is None
    assert get_age_carbon_14_dating(-1) is None
    assert get_age_carbon_14_dating("poopoo") is None

def test_calculate_stat():
    mean, sd = calculate_stat([65, 78, 89, 100])
    assert math.isclose(sd, 12.98, rel_tol=.01)
    assert math.isclose(mean, 83.00, rel_tol=.01)

def test_extract_position():
    assert extract_position('|update| the positron location in the particle accelerator is x:21.432') == '21.432'
    assert extract_position('debug x:32432.234') is None
    assert extract_position('') is None
