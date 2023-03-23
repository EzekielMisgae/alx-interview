#!/usr/bin/python3

""" Contains makeChange function"""

def makeChange(coins, total):
    if not coins:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if total == 0:
            return change
    return -1