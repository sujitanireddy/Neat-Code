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

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    window = set()

    L = 0
    for R in range(len(nums)):

        if (R - L) + 1 > k + 1:
            window.remove(nums[L])
            L+=1

        if nums[R] in window:
            return True

        window.add(nums[R])

    return False




        



print(containsNearbyDuplicate(nums=[1,2,1,2], k=3))