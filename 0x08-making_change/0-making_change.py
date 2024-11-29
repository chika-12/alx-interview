#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Parameters:
        coins (list): List of coin denominations.
        total (int): Target total amount.

    Returns:
        int: Fewest number of coins needed to meet total.
             -1 if the total cannot be met using the given coins.
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for a total of 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
