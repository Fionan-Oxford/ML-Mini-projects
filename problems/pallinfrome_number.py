"""Given an integer x, return true if x is a palindrome, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

import math


class Solution:
    def isPalindrome(self, x: int) -> bool:

        num_string = str(x)
        n = len(num_string)
        mid = math.ceil(n / 2) - 1  # 0 indexing
        print(mid)

        if n % 2 == 0:
            string_start, string_end = num_string[0 : mid + 1], num_string[mid + 1 :]
        else:
            string_start, string_end = num_string[0:mid], num_string[mid + 1 :]

        print(string_start)
        print(string_end)

        return True if string_start[::-1] == string_end else False


x = 1122333454332211
mySolution = Solution()
print(mySolution.isPalindrome(x))
