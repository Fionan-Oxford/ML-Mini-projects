"""Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters."""


class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = 0
        output = ""

        for i, l in enumerate(s):
            this_longest_even = 0
            this_longest_odd = 1

            start = s[0:i]
            pivot = l
            end = s[i + 1 :]

            # Case even palindrome (center between i and i+1)
            start_even = (start + pivot)[::-1]
            for j in range(min(len(start_even), len(end))):
                if start_even[j] == end[j]:
                    this_longest_even += 1
                else:
                    break

            if this_longest_even > 0:
                even_len = 2 * this_longest_even
                l_idx = i - this_longest_even + 1
                r_idx = i + this_longest_even
                if even_len > longest:
                    output = s[l_idx : r_idx + 1]
                    longest = even_len

            # Case odd palindrome (center at i)
            start_rev = start[::-1]
            for j in range(min(len(start_rev), len(end))):
                if start_rev[j] == end[j]:
                    this_longest_odd += 1
                else:
                    break

            odd_len = 2 * this_longest_odd - 1
            l_idx = i - (this_longest_odd - 1)
            r_idx = i + (this_longest_odd - 1)
            if odd_len > longest:
                output = s[l_idx : r_idx + 1]
                longest = odd_len

        return output


# quick checks
mySolution = Solution()
print(mySolution.longestPalindrome("babad"))  # "bab" or "aba"
print(mySolution.longestPalindrome("cbbd"))  # "bb"
