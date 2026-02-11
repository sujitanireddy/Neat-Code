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









print(dailyTemperatures_bruteforce(temperatures=[22,21,20]))