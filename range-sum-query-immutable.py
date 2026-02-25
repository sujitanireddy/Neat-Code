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

    #Time Complexity: Everytime sumRange is called, it's going to be O(1) as we precomputed the prefix sums
     
    def __init__(self, nums: list[int]):
        self.prefix_sums = []
        sum = 0
        for num in nums:
            sum += num
            self.prefix_sums.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        left_prefix = self.prefix_sums[left - 1] if left > 0 else 0  
        right_prefix = self.prefix_sums[right]
        return right_prefix - left_prefix