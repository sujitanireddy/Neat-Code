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
    
    """
    Intution: Watch this video -> https://www.youtube.com/watch?v=LPFhl65R7ww
    Alogrithm:
        - Binary search for a partition point in the smallest array of both given arrays
        - Validate if that partition point is valid.
        - If valid: return based on the len of the combined array
        - If not valid: Move pointers accordingly
    """
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        #we want to binary search the smallest array of both. So it's easy to always keep nums1 as the smallest of the both.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        l = 0
        r = m

        while l <= r:
            nums1_left_elements = (r + l) // 2
            nums2_left_elements = ((m + n + 1) // 2) - nums1_left_elements

            #if the elements to the left are 0. We are comparing with "-inf".
            #nums1[nums1_left_elements - 1] is grabbing the right most element in the left partition array.
            max_left_nums1 = float("-inf") if nums1_left_elements == 0 else nums1[nums1_left_elements - 1]
            max_left_nums2 = float("-inf") if nums2_left_elements == 0 else nums2[nums2_left_elements - 1]

            #if the elements to the right are 0. We are comparing with "inf". 
            #nums1[nums1_left_elements] is grabbing the left most element in the right partition array.
            min_right_nums1 = float("inft") if nums1_left_elements == m else nums1[nums1_left_elements] #if left side len is equal to m then no element is on the right side
            min_right_nums2 = float("inft") if nums2_left_elements == n else nums2[nums2_left_elements] #if left side len is equal to n then no element is on the right side


            #we found the partition point
            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                if (m + n) % 2 == 0:
                    return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2
                else:
                    return max(max_left_nums1, max_left_nums2)
            
            #moving the pointers accordingly
            if max_left_nums2 > min_right_nums1:
                l = nums1_left_elements + 1
            
            else:
                r = nums1_left_elements - 1




        

        
        
        







sol = Solution()
result = sol.findMedianSortedArrays(nums1 = [1,3,8,9,15], nums2 = [7,11,18,19,21,25])
print(result)

