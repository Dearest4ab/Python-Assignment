def calculate_discount(price, discount_percent):
    if discount_percent >= 20:   # Apply discount only if it's 20% or more
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price