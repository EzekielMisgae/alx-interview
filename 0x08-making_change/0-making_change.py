#!/usr/bin/python3
'''Making change challenge'''

def makeChange(coins, total):
    # Initialize a list to store the minimum number of coins needed for each total from 0 to the given total
    dp = [float('inf')] * (total + 1)
    # 0 coins are needed to make a total of 0
    dp[0] = 0
    # Iterate through each coin and update the minimum number of coins needed for each total
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    # If the minimum number of coins needed for the given total is still infinity, it means the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1