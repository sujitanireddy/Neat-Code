#Question -> https://neetcode.io/problems/eating-bananas/question?list=neetcode150
import math
class Solution:

    #Brute Force solution: Time Complexity: O(n**2) and it's not a accepted solution for this question.
    def minEatingSpeed_Brute(self, piles: list[int], h: int) -> int:

        #max speed at which koko can eat bananas. We are trying to find min_speed: so knowing the max helps us find the upper bound
        max_speed = max(piles)
        min_speed = 1

        while min_speed <= max_speed:

            time_taken = 0

            for pile in piles:

                time_taken += math.ceil(pile/min_speed)
            
            if time_taken <= h:
                    return min_speed
            
            min_speed +=1




    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        def time_taken(mid):

            time_taken = 0
            
            for pile in piles:
                time_taken += math.ceil(pile/mid)
            
            return time_taken

        #we know the range: 1 to max_speed. As we know the range we can apply binary search here.
        right = max(piles)
        left = 1

        while left < right:
             
            mid = (left + right) // 2

            if time_taken(mid) > h:
                left = mid + 1
            
            else:
                right = mid
        
        return left



#Testing
sol = Solution()
result = sol.minEatingSpeed([25,10,23,4], h = 4)
print(result)

        
        