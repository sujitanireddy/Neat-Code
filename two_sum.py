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

#Two Sum - Two pointer method if the nums is sorted 
#Time Complexity: O(n)
def twoSum(nums: list[int], target: int) -> list[int]:

    L, R = 0, len(nums) - 1

    while L < R:

        if nums[L] + nums[R] > target:
            R -= 1
        
        elif nums[L] + nums[R] < target:
            L += 1
        
        else:
            return[L, R]
