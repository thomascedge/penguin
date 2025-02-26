from .utils.utils import Calculator

from .utils.model import Receipt, Item

import pytest

calculator = Calculator()

items_list = [
        Item(shortDescription='Mountain Dew 12PK', price='6.49'),
        Item(shortDescription='Emils Cheese Pizza', price='12.25'),
        Item(shortDescription='Knorr Creamy Chicken', price='1.26'),
        Item(shortDescription='Doritos Nacho Cheese', price='3.35'),
        Item(shortDescription='   Klarbrunn 12-PK 12 FL OZ  ', price='12.00')
    ]

receipt0 = Receipt(
    retailer='Target',
    purchaseDate='2022-01-01',
    purchaseTime='15:00',
    items=items_list,
    total='35.00'
)

receipt1 = Receipt(
    retailer='Target',
    purchaseDate='2022-01-02',
    purchaseTime='13:01',
    items=items_list,
    total='35.35'
)

def test_get_alpha():
    assert isinstance(calculator._get_alpha(receipt0.retailer), int) # Target
    assert calculator._get_alpha(receipt0.retailer) == 6 # Target

def test_get_cents():
    assert isinstance(calculator._get_cents(receipt0.total), int) # 35.00
    assert calculator._get_cents(receipt0.total) == 50 # 35.00
    assert calculator._get_cents(receipt1.total) == 0 # 35.35

def test_get_multiple_of_25():
    assert isinstance(calculator._get_multiple_of_25(receipt0.total), int) # 35.00
    assert calculator._get_multiple_of_25(receipt0.total) == 25 # 35.00
    assert calculator._get_multiple_of_25(receipt1.total) == 0 # 35.35

def test_get_every_two_items():
    assert isinstance(calculator._get_every_two_items(receipt0.items), int)
    assert calculator._get_every_two_items(receipt0.items) == 10

def test_get_trimmed_length():
    assert isinstance(calculator._get_trimmed_length(receipt0.items), int)
    assert calculator._get_trimmed_length(receipt0.items) == 6

# def test_get_llm():
#     assert isinstance(calculator._get_llm(), int)
#     assert calculator._get_llm()

def test_get_odd_date():
    assert isinstance(calculator._get_odd_date(receipt0.purchase_date), int) # 2022-01-01
    assert calculator._get_odd_date(receipt0.purchase_date) == 6 # 2022-01-01
    assert calculator._get_odd_date(receipt1.purchase_date) == 0 # 2022-01-02

def test_get_time_purchase():
    assert isinstance(calculator._get_time_purchase(receipt0.purchase_time), int) # 15:00
    assert calculator._get_time_purchase(receipt0.purchase_time) == 10 # 15:00
    assert calculator._get_time_purchase(receipt1.purchase_time) == 0 # 13:01
