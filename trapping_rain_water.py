#Question -> https://neetcode.io/problems/trapping-rain-water/question

#Brute Force Way
#Time Complexity - O(n**2)
"""
Algorithm: Find the water trapped at each index and sum them up.
    - To find the water trapped at each index we need the max height to the left and max height to the right of the index.
    - We can do that by initalizing two pointers at height[i] and then finding the max to the left and right.
    - Once we have the max the formaula is min(max_left, max_right) - height[i]
"""

def trap(height: list[int]) -> int:

    rain_trapped = 0

    for i in range(len(height)):

        max_right_height = max_left_height = height[i]

        for j in range(i):

            max_left_height = max(max_left_height, height[j])
        
        for j in range(i+1, len(height)):

            max_right_height = max(max_right_height, height[j])
        
        rain_trapped += min(max_right_height, max_left_height) - height[i]
    
    return rain_trapped


print(trap(height=[0,1,0,2,1,0,1,3,2,1,2,1]))


    