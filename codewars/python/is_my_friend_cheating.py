def remov_nb(n):
    """
    Is my friend cheating?
    
    Находит все пары чисел (a, b) в последовательности от 1 до n такие,
    что произведение a * b равно сумме последовательности без этих чисел.

    URL: https://www.codewars.com/kata/5547cc7dcad755e480000004/
    Date: 23.09.2025
    
    Args:
        n (int): Верхняя граница последовательности (1 до n включительно)
        
    Returns:
        list: Список кортежей пар чисел [(a, b), ...] в порядке возрастания a,
              либо пустой список, если таких пар нет
    """
    total = n * (n + 1) / 2
    list_nums_pairs = set()
    for a in range(int(n/2), n + 1):
        b = (total - a) / (a + 1)
        if not (b % 1) and b < n:
            list_nums_pairs.add((a, b))
            list_nums_pairs.add((b, a))
    return sorted(list(list_nums_pairs), key=lambda i: (i[0], i[1]))