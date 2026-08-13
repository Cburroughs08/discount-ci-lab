from discount import calculate_discounted_price
import pytest

def test_premium_discount():
    assert calculate_discounted_price(100, "premium") == 80.00

def test_standard_discount():
    assert calculate_discounted_price(100, "standard") == 90.00

def test_negative_price_raises():
    with pytest.raises(ValueError):
        calculate_discounted_price(-10, "standard")

def test_save10_coupon():
    assert calculate_discounted_price(100, "standard", coupon_code="SAVE10") == 81.00

def test_holiday_discount():
    assert calculate_discounted_price(100, "guest", is_holiday=True) == 95.00