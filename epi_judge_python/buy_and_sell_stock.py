from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            new_profit = prices[j] - prices[i]
            if new_profit > profit:
                profit = new_profit

    return profit


def test(prices: List[float], expected):
    actual = buy_and_sell_stock_once(prices)
    assert actual == expected, f"{prices}, expected {expected}, got {actual}"
    print(f"Passed {prices} == {expected}.")


if __name__ == '__main__':
    test([], 0)
    test([1, 2], 1)
    test([2, 1], 0)
    test([2, 1, 2], 1)
    test([1, 5], 4)
    test([1, 5, 4, 10], 9)
    test([5, 4, 10, 1], 6)

    #exit()

    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
