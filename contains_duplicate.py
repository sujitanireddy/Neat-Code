#Question - https://neetcode.io/problems/duplicate-integer/question?list=neetcode150


#Brute Force Approach
#Time Complexity: O(n**2)
def hasDuplicate_bruteforce(nums: list[int]) -> bool:
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


#Set buit-in data structure and loop method 
#Time Complexity: O(n)
def hasDuplicate_set_singleloop(nums: list[int]) -> bool:

    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False


#In-Built Length function using set
#Time Complexity: O(n)
def hasDuplicate_set_length(nums: list[int]) -> bool:

    if len(set(nums)) == len(nums):
        return False
    return True


#Sorting and single loop method
def hasDuplicate_sorting_singleloop(nums: list[int]) -> bool:

    sorted_nums = sorted(nums)

    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i-1]:
            return True
    return False

