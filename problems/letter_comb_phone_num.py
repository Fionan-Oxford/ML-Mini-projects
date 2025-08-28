"""
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        nd = len(digits)
        if nd == 0:
            return []

        lookup: dict[str, str] = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": " ",
        }
        letters = [lookup[d] for d in digits]
        comb: List[str] = []

        def dfs(path: str) -> None:

            n = len(path)

            if n == nd:
                comb.append(path)  # Appropiate length, append
                return

            this_digit = letters[n]
            for l in this_digit:
                path += l
                dfs(path)
                path = path[0:-1]

        dfs("")
        return comb


digits = "23"
mySolution = Solution()
print(mySolution.letterCombinations(digits))
