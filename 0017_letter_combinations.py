class Solution:
    mapping = {
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m','n','o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9': ['w','x','y','z']
    }

    def letterCombinations(self, digits: str) -> list:
        return self._combinations(digits)


    def _combinations(self, digits: str) -> list:
        if not digits:
            return None
        
        c = digits[0]
        digits = digits[1:]
        m = self.mapping[c]
        ret = self._combinations(digits)
        
        if not ret:
            return m
        return [i+j for i in m for j in ret]

if __name__ == "__main__":
    s = Solution()
    r = s.letterCombinations('234')
    print (r)

