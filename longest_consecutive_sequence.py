#Question -> https://neetcode.io/problems/longest-consecutive-sequence/question?list=neetcode150

import collections

#Time complexity 0(nlogn) as using sorting. Should solve in O(n)
def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    sorted_nums = sorted(set(nums))

    best = 1
    streak = 1

    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i - 1] + 1:
            streak += 1
        else:
            best = max(best, streak)
            streak = 1

    best = max(best, streak)
    return best

#Neet Solution O(n)
def longestConsecutive_neet(nums: list[int]) -> int:

    nums_set = set(nums)
    longest = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            length = 1
            while (num + length) in nums_set:
                length += 1
            longest = max(length, longest)
    return longest


    



print(longestConsecutive_neet(nums=[2,20,4,10,3,4,5]))