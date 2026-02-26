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


#Intution - Find the prefix product in one array. Postfix product in one array and multiply them.
class Solution:
    def productExceptSelf_revision_twoarraymethod(self, nums: list[int]) -> list[int]:

        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n
        output = [0] * n

        #The prefix of the first element will always be 1 
        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        
        #The last element in postfix array will always be 1.
        postfix[n-1] = 1
        for i in range(n-2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i+1]

        for i in range(n):
            output[i] = prefix[i] * postfix[i]

        return output
        
        

        




sol = Solution()
result = sol.productExceptSelf_revision_twoarraymethod(nums=[1,2,4,6])
print(result)