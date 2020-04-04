# 一次遍历，遍历的时候查询map
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i

        for i in range(len(nums)):
            num = target-nums[i]
            if num in map:
                j = map[num]
                if j > i:
                    return [i, j]
        return []

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9) == [0, 1])

print(s.twoSum([2, 7, 11, 15], 9) == [0, 2])

print(s.twoSum([2, 7, 11, 15], 13) == [0, 2])

print(s.twoSum([2,5,5,11], 10) == [1, 2])
