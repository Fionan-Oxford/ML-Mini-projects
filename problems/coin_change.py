"""
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Base case,
        if amount == 0:
            return 0

        # if it's in the coins return one
        elif amount in coins:
            return 1

        # find the largest coin that's less than amount
        try:
            largest_coin = max([coin for coin in coins if coin < amount])
        except:
            return -1

        return self.coinChange(coins, amount - largest_coin) + 1


mySolution = Solution()
coins = [2]
amount = 3
print(mySolution.coinChange(coins, amount))
