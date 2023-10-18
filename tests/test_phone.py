import pytest
from src.phone import Phone

def test_number_of_sim_valid_value():
    phone = Phone("iPhone", 1000, 10, 2)
    assert phone.number_of_sim == 2

def test_number_of_sim_invalid_value():
    with pytest.raises(ValueError):
        Phone("iPhone", 1000, 10, 0)

def test_add_method():
    phone1 = Phone("iPhone1", 1000, 5, 2)
    phone2 = Phone("iPhone2", 1500, 3, 1)
    result = phone1 + phone2
    assert result == 8