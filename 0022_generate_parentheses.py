class Solution:
    def generateParenthesis(self, n: int) -> list:
        ans = []
        def g(s = '', leftCount = 0, rightCount = 0) -> list:
            if (leftCount == rightCount == n):
                ans.append(s)
                return
                
            if leftCount < n:
                g(s+'(', leftCount+1, rightCount)
            if rightCount < leftCount:
                g(s+')', leftCount, rightCount+1)

        g()
        return ans
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
