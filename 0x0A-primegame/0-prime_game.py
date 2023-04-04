#!/usr/bin/python3

def isWinner(x, nums):
    wins = {"Maria": 0, "Ben": 0}
    for n in nums:
        if n == 1:
            wins["Ben"] += 1  # Ben wins immediately if n is 1
        elif n % 2 == 0:
            wins["Ben"] += 1  # Ben wins if n is even
        else:
            wins["Maria"] += 1  # Maria wins if n is odd
    return max(wins, key=wins.get) if wins else None

