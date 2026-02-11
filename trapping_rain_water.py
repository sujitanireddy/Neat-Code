#Question -> https://neetcode.io/problems/trapping-rain-water/question

#Brute Force Way
#Time Complexity - O(n**2)
"""
Algorithm: Find the water trapped at each index and sum them up.
    - To find the water trapped at each index we need the max height to the left and max height to the right of the index.
    - We can do that by initalizing two pointers at height[i] and then finding the max to the left and right.
    - Once we have the max the formaula is min(max_left, max_right) - height[i]
"""

def trap_brute_force(height: list[int]) -> int:

    rain_trapped = 0

    for i in range(len(height)):

        max_right_height = max_left_height = height[i]

        for j in range(i):

            max_left_height = max(max_left_height, height[j])
        
        for j in range(i+1, len(height)):

            max_right_height = max(max_right_height, height[j])
        
        rain_trapped += min(max_right_height, max_left_height) - height[i]
    
    return rain_trapped


#Time Complexity: O(n)
#Space Complexity: O(n)
"""
Algorithm: Find the water trapped at each indexand sum them up (Reference -> https://neetcode.io/problems/trapping-rain-water/solution)
    - Basically the same algoritm as the brute force method, however we save the min and max heights for each position so that we don't have to compute every single time.
    - This approach will drop the time complexity to liner time, however takes extra space for saving the arrays.
"""
def trap(height: list[int]) -> int:

    length = len(height)

    #building left max array
    left_max = [0] * length
    left_max_so_far = 0
    for i in range(1, length):
        left_max_so_far = max(left_max_so_far, height[i-1])
        left_max[i] = left_max_so_far
    
    #building right max array
    right_max = [0] * length
    right_max_so_far = 0
    for j in range(length - 2, -1, -1):
        right_max_so_far = max(right_max_so_far, height[j+1])
        right_max[j] = right_max_so_far

    #computing water trapped at each index
    water_trapped_at_each_index = []
    for i in range(length):
        water_trapped = min(left_max[i], right_max[i]) - height[i]
        if water_trapped < 0:
             water_trapped_at_each_index.append(0)
        else:
            water_trapped_at_each_index.append(water_trapped)
    return sum(water_trapped_at_each_index)


#Most Optimal Way: Time Complexity: O(n), Space Complexity: O(1)
"""
Algorithm: Compute the water trapped at each index without additional space and sum it up.
    - We know that we need the minimun of both left and right heights as that's the max water we can trap.
    - Let's initiate two pointers: l = start, r = end
        - Until both of them meet:
            - keep track of the highest so far by moving the left and right pointers accordingly, so that we always know the minimum so far (and min is what we care about)
            - keep adding to the water trapped so far
"""

def trap_optimal(height):

    l, r = 0, len(height) - 1 
    max_left, max_right = height[l], height[r]
    water_trapped = 0

    while l < r:

        if max_left <= max_right:
            max_left = max(max_left, height[l])
            water_trapped += max_left - height[l]
            l +=1 
        else:
            max_right = max(max_right, height[r])
            water_trapped += max_right - height[l]
            r -=1
    
    return water_trapped



#Testing
print(trap_optimal(height=[0,1,0,2,1,0,1,3,2,1,2,1]))
