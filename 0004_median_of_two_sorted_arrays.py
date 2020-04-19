class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            m, n = n, m
            nums1, nums2 = nums2, nums1
        
        imin, imax = 0, m
        while imin <= imax:
            i = (imin+imax) // 2
            j = (m + n) // 2 - i

            if i < m and nums2[j-1] > nums1[i]:
                # i too small
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i too big
                imax = i - 1
            else:
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                if ((n+m) % 2) == 1:
                    return min_of_right
                else:
                    if i == 0:
                        max_of_left = nums2[j-1]
                    elif j == 0:
                        max_of_left = nums1[i-1]
                    else:
                        max_of_left = max(nums1[i-1], nums2[j-1])
                    return (max_of_left+min_of_right) / 2


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1,2,3,4], []))
    print(sol.findMedianSortedArrays([], [2,3]))
    print(sol.findMedianSortedArrays([1,3], [2]))
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))
