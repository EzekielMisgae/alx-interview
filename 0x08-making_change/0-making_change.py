#!/usr/bin/python3
"""
Contains making change challenge:
"""


def makeChange(coins, total):
    """Find the minimum number of coins needed to make change for a given amount of money.
    
    Args:
        coins (list): A list of coin values.
        total (int): The total amount of money to make change for.
    
    Returns:
        The fewest number of coins needed to make change for the given amount of money. If change cannot be made, return -1.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    min_coins = [float("inf")] * (total + 1)

    # Base case: 1 coin needed to make change for its own value
    for coin in coins:
        if coin <= total:
            min_coins[coin] = 1

    # For each amount from 1 to total, calculate the minimum number of coins needed
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[total] if min_coins[total] != float("inf") else -1
