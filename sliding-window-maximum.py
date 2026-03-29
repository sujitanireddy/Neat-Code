#Question -> https://neetcode.io/problems/sliding-window-maximum/question

import collections

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:

    L = 0
    q = collections.deque()
    output = []

    for R in range(len(nums)):

        #if the top of the deck is less than current number. We don't need to track the number anymore in our deck
        while q and nums[q[-1]] < nums[R]:
            q.pop()

        q.append(R)

        #if left is out of bounds. Remove it from deck
        if q[0] < L:
            q.popleft()

        #if we are over the window then move Left pointer and add it left most element to output
        if (R - L) + 1 == k:
            output.append(nums[q[0]])
            L += 1
    
    return output
















print(maxSlidingWindow(nums = [5, 1, 2, 3, 4], k = 2))

        