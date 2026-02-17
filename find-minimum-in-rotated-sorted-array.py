#Question -> https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/question?list=neetcode150

class Solution:

    #BruteForce: TimeComplexity: O(n)
    def findMin_bruteforce(self, nums: list[int]) -> int:
        return min(nums)
    

    """
        Intution:
        A rotated sorted array consists of two sorted subarrays.
        Example: [3, 4, 5, 1, 2]

        We can use binary search to determine which side contains the minimum
        element. At any step, one half of the array is guaranteed to be sorted.

        Key idea:
        - If nums[l] < nums[r], the current portion is already sorted.
        In that case, nums[l] is the minimum.
        - Otherwise, we use the middle element to determine which half
        contains the rotation point (minimum element).

        Algorithm:
        while l < r:

            if you found a sorted array.
                break and return the left pointer

        binary search with comparing mid to left pointer to decide which part of the array to check and proceed with for further binary search.  
    """
    def findMin(self, nums: list[int]) -> int:

        l, r = 0, len(nums) - 1
        result = nums[0]

        while l <= r:

            #if the array is already sorted
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break

            mid = (l + r) //2

            if nums[mid] >= nums[l]:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return result
    


#testing
sol = Solution()
result = sol.findMin([4,5,6,7])
print(result)

        
        
        