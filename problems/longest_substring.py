"""Given a string s,
find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring."""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sub_string = ""
        count = 0
        longest_count = 0

        for l in s:
            if l not in sub_string:
                count += 1
                sub_string += l
                if count > longest_count:
                    longest_count = count
            else:  # we have a clash
                _, sub_string = sub_string.split(l)
                sub_string += l
                count = len(sub_string)

        return longest_count


s = "pwwkew"
mySolution = Solution()
print(mySolution.lengthOfLongestSubstring(s))
