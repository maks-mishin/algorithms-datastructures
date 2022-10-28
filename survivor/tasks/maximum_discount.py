def MaximumDiscount(things_count: int, price: list) -> int:
    """Return maximum discount on given number of things"""
    if things_count < 3:
        return 0
    SET_THINGS = 3
    max_discount_1, max_discount_2 = 0, 0
    count_free_things = things_count // 3
    
    price.sort(reverse=True)
    max_discount_1 = sum([price[-i] for i in range(1, count_free_things + 1)])
    
    while len(price) >= SET_THINGS:
        max_discount_2 += min(price[:SET_THINGS])
        price = price[SET_THINGS:]
    return max(max_discount_1, max_discount_2)
