#!/usr/bin/python3
"""A function to determine the fewest number of coins needed
   to meet a given amount total"""


def makeChange(coins, total):
    """This function will take a list of coins and use
       that to calculate how much change the total will require
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
=======
#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Create a table to store the minimum number of coins
    for each sub-total"""
    if total <= 0:
        return 0
    """    The table is initialized with a large value (total + 1)
    for sub-totals
    that cannot be achieved
    """
    min_coins = [total + 1] * (total + 1)
    min_coins[0] = 0

    """Iterate over all sub-totals from 1 to the given total"""
    for sub_total in range(1, total + 1):
        """Try each coin value and see if it can be used to make
        the sub-total"""
        for coin in coins:
            if coin <= sub_total:
                """If the coin can be used, update the minimum
                number of coins needed"""
                min_coins[sub_total] = min(min_coins[sub_total],
                                           1 + min_coins[sub_total - coin])

    """If the final entry in the table has not been updated,
    it means the total cannot be achieved"""
    if min_coins[total] > total:
        return -1
    else:
        return min_coins[total]