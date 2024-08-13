# Source: https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/python

from itertools import combinations


def choose_best_sum(t, k, ls):
    list_comb = [sum(comb) for comb in combinations(ls, k)]
    if not list_comb:
        return None
    if min(list_comb) > t:
        return None
    return max(filter(lambda d: d <= t, list_comb))
