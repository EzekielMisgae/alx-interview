#!/usr/bin/python3
'''Making change challenge'''


def makeChange(coins, total):
    # Initialize a list to store the minimum number of coins needed for each total from 0 to the given total
    if not coins or coins is None:
        return -1
    # 0 coins are needed to make a total of 0
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    # Initialize a list to store the minimum number of coins needed for each total from 0 to the given total
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            # If the minimum number of coins needed for the given total is still infinity, it means the total cannot be met
            return change
    return -1
