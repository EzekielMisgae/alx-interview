#!/usr/bin/python3
"""
This code provides a solution to the Prime Game problem.
"""

def primes(n):
    """Return a list of prime numbers between 1 and n inclusive"""
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game
    
    Args:
    x (int): the number of rounds of the game
    nums (list): a list of integers that are the upper limits of range for each round
    
    Return:
    The name of the winner (Maria or Ben) or None if the winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    else:
        return None
