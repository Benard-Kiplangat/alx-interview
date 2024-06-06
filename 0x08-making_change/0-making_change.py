#!/usr/bin/python3
"""A script that calculates the minimal amount of change"""


def makeChange(coins, total):
    """The makeChange function to calculate the number of coins
        Args:
            coins: the value of coins available
            total: the total amount
    """

    if (total <= 0):
        return 0

    """First sort the coins in descending order"""
    coins.sort(reverse=True)

    amountChecked = 0
    numberCoins = 0

    for i in coins:
        while amountChecked < total:
            amountChecked = amountChecked + i
            numberCoins = numberCoins + 1
        if amountChecked == total:
            return numberCoins
        amountChecked = amountChecked - i
        numberCoins = numberCoins - 1

    return -1
