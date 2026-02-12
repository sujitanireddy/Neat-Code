#Question -> https://neetcode.io/problems/car-fleet/question?list=neetcode150
#Time Complexity: O(n)
#Space Complexity: 
"""
Algorithm: We need to compute the time taken to reach the target in desc order of the positions from the target.
- Time Taken formule: (target - position) / speed
- Just computing time is not enough, we now need to find out all the cars which will form a fleet due to being faster than the one forward. For that a stack can be really helpful
Note: The reason we zip the postion and speed together is to calculate the time taken in desc order, doing it this way is much simpler.
"""

def carFleet(target: int, position: list[int], speed: list[int]) -> int:

    stack = []

    #list of position and speed tuples
    pos_speed = list(zip(position, speed))

    pos_speed.sort(reverse=True) #Descending order of positions

    for p, s in pos_speed:

        stack.append((target - p) / s)

        #at this point we want to check if the first speed appended is lower or equal than the next speed being appended, if it is they are going to collide. So we pop our existing one.

        if len(stack) >= 2 and stack[-1] <= stack[-2]:

            stack.pop()
    
    return len(stack)


#for testing
print(carFleet(target=12, position=[10,8,0,5,3],speed=[2,4,1,1,3]))
        
