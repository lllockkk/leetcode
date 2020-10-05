class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        results = []
        l = len(nums)
        for i in range(l):
            # 去重
            if i > 0 and nums[i]==nums[i-1]:
                continue

            j = i + 1
            k = l - 1
            while j < k:
                # 去重
                if j>i+1 and nums[j]==nums[j-1]:
                    j=j+1
                    continue
                if k<l-1 and nums[k]==nums[k+1]:
                    k=k-1
                    continue
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    results.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    k=k-1
                elif sum < 0:
                    j=j+1
                else:
                    k=k-1
        
        return results

def printResults(r):
    for i in r:
        for j in i:
            print(j, end=' ')
        print()

if __name__ == "__main__":
    s = Solution()
    
    r = s.threeSum([0,0,0])
    printResults(r)

    r = s.threeSum([-1, 0, 1, 2, -1, -4])
    printResults(r)

    r = s.threeSum([-2,0,0,2,2])
    printResults(r)

