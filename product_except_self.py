# Question -> https://neetcode.io/problems/products-of-array-discluding-self/question?list=neetcode150


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        #claculating the prefix array
        prefix = 1
        output_array = [1]

        for i in range(len(nums)-1):

            output_array.append(prefix * nums[i])

            prefix *= nums[i]
        
        
        #calculating the postfix array while multiplying 
        postfix = 1

        for i in range (len(nums) -1 ,-1 ,-1):

            output_array[i] *= postfix

            postfix *= nums[i]


        return output_array


