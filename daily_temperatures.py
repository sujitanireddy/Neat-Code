# Question -> https://neetcode.io/problems/daily-temperatures/question

#BruteForce Approach. Time Complexity: O(n**2) Space Complexity: O(n)
"""
Algorithm: For every temp calculate the next greater value using a double loop approach.
"""
def dailyTemperatures_bruteforce(temperatures: list[int]) -> list[int]:

    length = len(temperatures)
    result = [0] * length

    for i in range(length):
        for j in range(i+1, length):
            
            if temperatures[j] > temperatures[i]:

                result[i] = j - i

                break
    
    return result


"""
Algorithm: Using a stack we can keep track of the (temp,idx) and whenever we find a higher temp while traversing. Pop the element and find the 
diffrence btw the current idx and popped idx.

Basically the core formule is the same a the brute force -> Higher temp idx - current temp idx, but we are acheiving this using a stack reducing
the time complixty from O(n**2) to O(n)

The video was helpful in understanding the stack solution -> https://www.youtube.com/watch?v=_ZEvmycwXHs 
"""

def dailyTemperatures_stack(temperatures: list[int]) -> list[int]:

    stack = []
    n = len(temperatures)
    result = [0] * n

    for i, t in enumerate(temperatures):

        #while stack is not emptpy and the temp in stack is less than current temp: we found a higher temp 
        while stack and stack[-1][0] < t:

            stk_temp, stk_idx = stack.pop()

            result[stk_idx] = i - stk_idx

        stack.append((t,i))
    
    return result



    
    








#testing
print(dailyTemperatures_stack(temperatures=[30,38,30,36,35,40,28]))