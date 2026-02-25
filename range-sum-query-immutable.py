#Question -> https://neetcode.io/problems/range-sum-query-immutable/history?list=neetcode150&submissionIndex=0

class NumArray:

    #Time Complexity: Everytime sumRange is called, it's going to take O(n) time.
    #What if we pre-compute the pre-fix sum so that we can solve sumRange in O(n)
    #Prefix sum alogorithm -> https://neetcode.io/courses/advanced-algorithms/4

    #bruteforce approach
    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right+1):
            sum += self.nums[i]
        return sum
    

class NumArray_optimal:
     
    def __init__(self, nums: list[int]):
        pass

    def sumRange(self, left: int, right: int) -> int:
        pass