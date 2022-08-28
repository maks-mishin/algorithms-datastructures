# Source: 

import unittest


def moving_average(timeseries: list, K: int) -> list:
    result = []
    for begin_index in range(0, len(timeseries) - K + 1):
        end_index = begin_index + K
        current_sum = 0
        for i in range(begin_index, end_index):
            current_sum += timeseries[i]
        current_avg = current_sum / K
        result.append(round(current_avg, 2))
    return result


class TestMovingAverage(unittest.TestCase):
    def test_moving_average(self):
        pass


if __name__ == "__main__":
    unittest.main()
