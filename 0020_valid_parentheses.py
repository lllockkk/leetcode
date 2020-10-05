class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        pair = {'(':')', '[':']', '{':'}'}
        l = []
        for c in s:
            if c in {'(','[','{'}:
                l.append(c)
            elif len(l) == 0 or pair[l.pop()] != c:
                return False
        
        return len(l) == 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid(''), True)
    print(sol.isValid('()[]{}'), True)
    print(sol.isValid('(}'), False)
    print(sol.isValid('([{}])'), True)
    print(sol.isValid('([{}]))'), False)
