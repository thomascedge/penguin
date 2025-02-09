from utils import Utils

import pytest

util = Utils()
test_data = {
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseDate_0": "2022-01-01",
  "purchaseDate_1": "2022-01-02",
  "purchaseTime": "13:01",
  "purchaseTime_0": "15:00",
  "purchaseTime_1": "13:01",
  "items": [
    {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
    {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
    {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
    {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
    {"shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00"}
  ],
  "total": "35.35",
  "total_0": "35.00",
  "total_1": "35.35"
}

def test_get_alpha():
    assert isinstance(util._get_alpha(test_data['retailer']), int) # Target
    assert util._get_alpha(test_data['retailer']) == 6 # Target

def test_get_cents():
    assert isinstance(util._get_cents(test_data['total_0']), int) # 35.00
    assert util._get_cents(test_data['total_0']) == 50 # 35.00
    assert util._get_cents(test_data['total_1']) == 0 # 35.35

def test_get_multiple_of_25():
    assert isinstance(util._get_multiple_of_25(test_data['total_0']), int) # 35.00
    assert util._get_multiple_of_25(test_data['total_0']) == 25 # 35.00
    assert util._get_multiple_of_25(test_data['total_1']) == 0 # 35.35

def test_get_every_two_items():
    assert isinstance(util._get_every_two_items(test_data['items']), int)
    assert util._get_every_two_items(test_data['items']) == 10

def test_get_trimmed_length():
    assert isinstance(util._get_trimmed_length(test_data['items']), int)
    assert util._get_trimmed_length(test_data['items']) == 6

def test_get_llm():
    assert isinstance(util._get_llm(), int)
    assert util._get_llm()

def test_get_odd_date():
    assert isinstance(util._get_odd_date(test_data['purchaseDate_0']), int) # 2022-01-01
    assert util._get_odd_date(test_data['purchaseDate_0']) == 6 # 2022-01-01
    assert util._get_odd_date(test_data['purchaseDate_1']) == 0 # 2022-01-02

def test_get_time_purchase():
    assert isinstance(util._get_time_purchase(test_data['purchaseTime_0']), int) # 15:00
    assert util._get_time_purchase(test_data['purchaseTime_0']) == 10 # 15:00
    assert util._get_time_purchase(test_data['purchaseTime_1']) == 0 # 13:01
