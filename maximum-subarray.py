#Question -> https://neetcode.io/problems/maximum-subarray/question
#Algorithm - Kandane's Algorithm for effecient solution
#Video - https://www.youtube.com/watch?v=hLPkqd60-28
"""
The idea of Kadane's algorithm is to traverse over the array from left to right and for each element, find the maximum sum among all subarrays ending at that element. The result will be the maximum of all these values.
"""

class Solution:

    #Intution - Keep adding to the sum. If at any point the sum is less than 0. Reset and again keep adding.
    #If negative numbers are involved then keep track of the maximum so far. 

    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = float('-inf')
        cur_sum = 0

        for num in nums:
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        
        return max_sum

sol = Solution()
result = sol.maxSubArray(nums=[-1])
print(result)