from src.item import Item
import pytest
from src.phone import Phone

def test_calculate_total_price():
    item = Item("Смартфон", 10000, 20)
    assert item.calculate_total_price() == 200000


def test_apply_discount():
    item = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000.0


def test_name_lenght():
    '''Длина имени не более 10'''
    item = Item('test1', 20.0, 5)
    item.name = 'This is long name'
    assert item.name == 'This is lo'


def test_string_to_number():
    assert Item.string_to_number('5') == 5


def test_str_magical():
    item = Item("Iphone", 10000, 20)
    assert str(item) == "Iphone"


def test_repr_magical():
    item = Item("Nokia3310", 10000, 20)
    assert repr(item) == "Item('Nokia3310', 10000, 20)"

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
