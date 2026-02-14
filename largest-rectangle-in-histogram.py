#Question -> https://neetcode.io/problems/largest-rectangle-in-histogram/question?list=neetcode150
#Brute Force Approach. Time Complexity: O(n**2), Space Complexity: O(n**2)
def largestRectangleArea_BruteForce(heights: list[int]) -> int:

    possible_areas = heights.copy()

    for i in range(len(heights)):

        l = float("inf")

        for j in range(i+1, len(heights)):

            l = min(l, heights[j], heights[i])
            b = (j - i) + 1
            possible_areas.append(l*b)

    return max(possible_areas)


"""
This video was helpful in understanding how the stack alogirthm works -> https://www.youtube.com/watch?v=ZGMw8Bvpwd4

Algorithm: Intution: can the height extend to the right? If it can it means that the bar is higher than what is on top of the stack currently, so we keep adding to the stack.
    - If the top of the stack height is < current height: it means that we cannot draw a rect as an extenstion, so we pop() and compute the area on the fly and update
    max area so far. (Note: We also have to update the idx of the top of the stack element to the popped index)
    - After traversing through the entire array and if there are still elements in the stack that means that these heights can be extended till the end.
        - So we just keep popping and comupting the area until the stack is empty
"""
#Time Complexity: O(n), Space Complexity: O(n)
def largestRectangleArea(heights: list[int]) -> int:

    stk = []
    n = len(heights)
    max_area = 0

    for i, h in enumerate(heights):

        #to keep track of start of the rect
        start = i

        while stk and h < stk[-1][0]:

            popped_h, popped_idx = stk.pop()

            max_area = max(max_area, popped_h * (i - popped_idx))

            start = popped_idx

        stk.append((h, start))


    while stk:

        popped_h, popped_idx = stk.pop()

        max_area = max(max_area, popped_h * (n - popped_idx))
    
    return max_area


print(largestRectangleArea(heights=[7,1,7,2,2,4]))