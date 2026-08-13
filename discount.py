def calculate_discounted_price(price, customer_type, coupon_code=None, is_holiday=False):
    """
    Calculate the final discounted price for a customer.

    Business rules:
    - premium customers receive 20% off
    - standard customers receive 10% off
    - guests receive no customer discount
    - coupon code SAVE10 gives an additional 10% off
    - coupon code SAVE20 gives an additional 20% off, but only for premium customers
    - holiday promotion gives an additional 5% off
    - discounts are applied sequentially
    - final price is rounded to 2 decimal places
    - price must be greater than or equal to 0
    - unknown customer types are treated as guests
    - unknown coupon codes are ignored
    """

    if price < 0:
        raise ValueError("price cannot be negative")

    customer_type = customer_type.lower()

    if customer_type == "premium":
        price = price * 0.8
    elif customer_type == "standard":
        price = price * 0.9

    if coupon_code == "SAVE10":
        price = price * 0.9
    elif coupon_code == "SAVE20" and customer_type == "premium":
        price = price * 0.8

    if is_holiday:
        price = price * 0.95

    return round(price, 2)