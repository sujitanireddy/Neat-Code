#Question -> https://neetcode.io/problems/largest-rectangle-in-histogram/question?list=neetcode150
#Brute Force Approach. Time Complexity: O(n**2), Space Complexity: O(n**2)
def largestRectangleArea(heights: list[int]) -> int:

    possible_areas = heights.copy()

    for i in range(len(heights)):

        l = float("inf")

        for j in range(i+1, len(heights)):

            l = min(l, heights[j], heights[i])
            b = (j - i) + 1
            possible_areas.append(l*b)

    return max(possible_areas)








print(largestRectangleArea(heights=[2,1,5,6,2,3]))