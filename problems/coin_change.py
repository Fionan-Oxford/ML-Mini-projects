"""
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

"""

from typing import List
from functools import lru_cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def solve(rem: int) -> int:
            if rem == 0:
                return 0
            if rem < 0:
                return amount + 1

            best = amount + 1
            for c in coins:
                best = min(best, solve(rem - c) + 1)
            return best

        ans = solve(amount)
        return -1 if ans == amount + 1 else ans


coins = [1, 2, 5]
amount = 100

mySolution = Solution()
print(mySolution.coinChange(coins, amount))
