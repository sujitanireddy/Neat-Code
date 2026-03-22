#Question -> https://neetcode.io/problems/contains-duplicate-ii/question?list=neetcode250

#BruteForce Approach
#Time Complexity: O(n**2)
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:

    for L in range(len(nums)):
        for R in range(L+1, min(len(nums), L + k + 1)):
            if nums[L] == nums[R]:
                return True
    
    return False

#Efficient way O(n)





        



print(containsNearbyDuplicate(nums=[1,2,1,2], k=3))