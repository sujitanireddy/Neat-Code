#Question -> https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode150

from collections import defaultdict


#O(n log n) solution
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


# Time Complexity: O(n) 
# Space Complexity: O(n)
def topKFrequent_efficient(nums: list[int], k: int) -> list[int]:

    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1
    
    buckets = []
    for _ in range(len(nums) + 1): #if we take 1 freq of each number the max freq buckets we would need are len(nums) + 1
        buckets.append([])

    for num, freq in freq_map.items():
        buckets[freq].append(num)
    
    output = []
    for i in range(len(buckets) -1 , 0, -1):
        for num in buckets[i]:
            output.append(num)
        if len(output) == k:
            return output










print(topKFrequent_efficient(nums=[7,8,8,9,9,9], k=2))