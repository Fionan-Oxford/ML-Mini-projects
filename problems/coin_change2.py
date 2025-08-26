"""
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount.
If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1 #
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1"""

# keep dropping down until you find a solution.
# When you do increase count by 1.
# problems, order would still increase by 1 for 5 + 5 + 1, vs 1 + 5 + 5

# for a solution for amount, we have as many solutions as amount - Coin, + 1 for each of the coins.
# Each op these have as many solutions as amount - coin + 1, for each of the coins.
# Keep decreasing back till we hit 0, or negative number (not viable)

# So no_of_s

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        if amount == 0:
            return 1

        dp: list[int] = [0] * (amount + 1)  # 0 counts as a coin
        dp[0] = 1

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]

        return dp[amount]


amount = 5
coins = [1, 2, 5]

mySolution = Solution()
print(mySolution.change(amount, coins))
