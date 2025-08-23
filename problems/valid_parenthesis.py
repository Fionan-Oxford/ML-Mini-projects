"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false
"""

# "(", ")", "{", "}", "[" and "]"

# If I open a bracket of a type, and subsequent opens of another type must be first close before I close the outer type


class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False  # Must be even

        open = {"(", "{", "["}
        pair: dict[str, str] = {"(": ")", ")": "(", "{": "}", "}": "{", "[": "]", "]": "["}
        stack: list[str] = []

        for l in s:
            if l in open:
                stack.append(l)

            else:
                if len(stack) == 0:
                    return False

                sl = stack.pop()
                if pair[sl] != l:
                    return False

        return True if len(stack) == 0 else False


mySolution = Solution()
print(mySolution.isValid("){"))
