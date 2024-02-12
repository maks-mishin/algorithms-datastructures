class TupleComparator(tuple):
    def __lt__(self, other):
        if self[1] == other[1]:
            return self[0] < other[0]
        return self[1] > other[1]


def make_dict(items: list) -> dict:
    result_dict = {}
    items_list = [item.split() for item in items]
    for name, amount in items_list:
        if name not in result_dict:
            result_dict[name] = int(amount)
            continue
        result_dict[name] += int(amount)
    return result_dict


def ShopOLAP(n: int, items: list) -> list:
    items_dict = make_dict(items)
    sorted_items = sorted(items_dict.items(), key=TupleComparator)
    result_list = [
        name + ' ' + str(amount) for name, amount in sorted_items
    ]
    return result_list
