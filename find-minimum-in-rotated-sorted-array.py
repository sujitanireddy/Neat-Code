#Question -> https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/question?list=neetcode150

class Solution:

    #BruteForce: TimeComplexity: O(nlogn)
    def findMin_bruteforce(self, nums: list[int]) -> int:
        return min(sorted(nums))
    
    def findMin(self, nums: list[int]) -> int:
        pass
        
        