# 动态规划 Daynamic Programming
# 自顶向下
class Solution2(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)



                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self._isMatch(s, p, 0, 0)

    def _isMatch(self, s, p, s_idx, p_idx) -> bool:
        pChar = self._charAt(p, p_idx)
        sChar = self._charAt(s, s_idx)

        if not pChar:
            return sChar is None

        pnChar = self._charAt(p, p_idx+1)
        # *
        if pnChar == '*':
            # * 不匹配字符串
            matched = self._isMatch(s, p, s_idx, p_idx+2)
            if matched:
                return True
            if (pChar == '.' and sChar) or pChar == sChar:
                # * 匹配字符串
                matched = self._isMatch(s, p, s_idx+1, p_idx)
                if matched:
                    return True
        else:
            if (pChar == '.' and sChar) or pChar == sChar:
                matched = self._isMatch(s, p, s_idx+1, p_idx+1)
                if matched:
                    return True

        return False

        
    def _charAt(self, s, idx):
        return s[idx] if len(s) > idx else None



if __name__ == "__main__":
    sol = Solution2()
    print(sol.isMatch("ab", ".*c") == False)
    print(sol.isMatch("", "") == True)
    print(sol.isMatch("", "a*") == True)
    print(sol.isMatch("a", "") == False)
    print(sol.isMatch("aa", "a") == False)
    print(sol.isMatch("aab", "a*b") == True)
    print(sol.isMatch("ab", ".*") == True)