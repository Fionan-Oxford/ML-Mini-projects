"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        comb: List[str] = []

        def dfs(path: str) -> None:

            np = len(path)

            if np == n * 2:  # Of valid length, check for validity
                if self.test_parenthesis(path):
                    comb.append(path)
                    return

            for l in "()":
                path += l
                if len(path) > n * 2:
                    break

                if path.count("(") > n or path.count(")") > n:
                    break  # pruning

                dfs(path)
                path = path[0:-1]

        dfs("")

        return comb

    def test_parenthesis(self, path: str) -> bool:

        stack = []

        try:
            for l in path:
                if l == "(":
                    stack.append(l)
                else:
                    stack.pop()
        except:
            return False

        return True if not stack else False


mySolution = Solution()

print(mySolution.generateParenthesis(3))
# Output: ["((()))","(()())","(())()","()(())","()()()"]
