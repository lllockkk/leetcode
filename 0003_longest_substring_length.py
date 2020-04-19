'''
Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        f = 0
        t = 0
        maxLen = 0
        for c in s:
            idx = m[c] if c in m else None
            if idx is not None and idx >= f:
                # 重复
                f = idx + 1

            maxLen = max(maxLen, t - f + 1)
            m[c] = t
            t += 1
        return maxLen


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring('abc'))
    print(sol.lengthOfLongestSubstring('bbbbb'))
    print(sol.lengthOfLongestSubstring('pwwkew'))
    # assert sol.lengthOfLongestSubstring('abc') == 3
    # assert sol.lengthOfLongestSubstring('bbbbb') == 1
    # assert sol.lengthOfLongestSubstring('pwwkew') == 3
