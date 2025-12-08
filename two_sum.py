#Question - https://neetcode.io/problems/two-integer-sum/question?list=neetcode150

#Brute Force
#Time Complexity: O(n**2)
def twoSum(nums: list[int], target: int) -> list[int]:
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


#Hashmap method to find the diffrence. 
#Time Complexity: O(n)
def twoSum(nums: list[int], target: int) -> list[int]:

    hashmap = {}

    for i in range(len(nums)):

        difference = target - nums[i]

        if difference in hashmap:

            return [hashmap[difference], i]
            
        else:

            hashmap[nums[i]] = i