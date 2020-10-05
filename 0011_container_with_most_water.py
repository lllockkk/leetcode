class Solution:
    def maxArea(self, height: list) -> int:
        l = len(height)
        i,j,max = 0,l-1,0
        while i < j:
            area = min(height[i],height[j]) * (j-i)
            if area > max:
                max = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]), '=', '49')
    print(sol.maxArea([1,2,3,4,5,6,7]), '=', '12')
