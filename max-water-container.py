#Question -> https://neetcode.io/problems/max-water-container/question

"""
Algorithm:
The idea is that we want to maximize our area. So moving the smaller height pointer to a bigger one is the only way to do it. 
"""

class Solution:
    def maxArea(self, heights: list[int]) -> int:

        max_area = 0 
        L = 0
        R = len(heights) - 1

        while L < R:

            area = min(heights[L], heights[R]) * (R - L)
            max_area = max(max_area, area)

            if heights[L] < heights[R]:
                L += 1
            
            else:
                R -= 1
        
        return max_area

