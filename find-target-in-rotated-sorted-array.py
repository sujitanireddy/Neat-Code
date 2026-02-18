#Question -> https://neetcode.io/problems/find-target-in-rotated-sorted-array/question?list=neetcode150

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        #standard binary_search
        def binary_search(array):
            l = 0
            r = len(array) - 1 

            while l <= r:
                m = (l + r) // 2
                if target > array[m]:
                    l = m + 1
                elif target < array[m]:
                    r = m - 1
                else:
                    return m

        #Finding the pivot
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
    
        pivot_point = l

        target_found_in_first_half = binary_search(nums[:pivot_point])
        target_found_in_second_half = binary_search(nums[pivot_point:])

        if target_found_in_first_half != None:
            return target_found_in_first_half
        elif target_found_in_second_half != None:
            return len(nums[:pivot_point]) + target_found_in_second_half
        else:
            return -1


        
















sol = Solution()
result = sol.search(nums = [3,4,5,6,1,2], target = 1)
print(result)
        
