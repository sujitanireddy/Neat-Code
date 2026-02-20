class Solution:
    #brute Force
    def findMedianSortedArrays_BruteForce(self, nums1: list[int], nums2: list[int]) -> float:

        nums1.extend(nums2)
        nums1.sort()

        n = len(nums1)

        if n == 1:
            return float(nums1[0])
        
        if n % 2 == 0: #length is even
            mid = n // 2
            return (nums1[mid - 1] + nums1[mid]) / 2
        
        else: #length is odd
            mid = n // 2
            return float(nums1[mid])


sol = Solution()
result = sol.findMedianSortedArrays_BruteForce(nums1 = [1,3], nums2 = [2,4])
print(result)

