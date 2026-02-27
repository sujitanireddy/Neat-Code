#Question -> https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode150

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
        
        sorted_hashmap = sorted(hashmap.items(), reverse = True, key = lambda x: x[1]) 

        output = []
        for i in range(k):
            output.append(sorted_hashmap[i][0])

        return output