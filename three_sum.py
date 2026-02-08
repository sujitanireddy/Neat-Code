#Three sum -> https://neetcode.io/problems/three-integer-sum/question
#Brute Force method 
#Time complexity: O(n**4)
#Space complexity: O(n**2)
def threeSum(self, nums: list[int]) -> list[list[int]]:

    triplets = []

    for i in range(len(nums) - 2):
        for j in range(i+1, len(nums) - 1):
            for k in range(j+1, len(nums)):

                if nums[i] + nums[j] + nums[k] == 0:

                    if sorted([nums[i], nums[j], nums[k]]) in triplets:
                        continue
                    else:
                        triplets.append(sorted([nums[i], nums[j], nums[k]]))
        
    return triplets