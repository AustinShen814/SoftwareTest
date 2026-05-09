def get_shipping_cost(weight):
    if weight <= 0:
        raise ValueError("重量必须大于 0")
    if weight > 50:
        raise ValueError("重量不能超过 50kg")

    if weight <= 2:
        return 10
    elif weight <= 10:
        return 20
    elif weight <= 30:
        return 35
    else:  
        return 50