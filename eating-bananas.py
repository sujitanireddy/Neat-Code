#Question -> https://neetcode.io/problems/eating-bananas/question?list=neetcode150
import math
class Solution:
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

            

            


























#Testing
sol = Solution()
result = sol.minEatingSpeed_Brute(piles = [25,10,23,4], h = 4)
print(result)

        
        