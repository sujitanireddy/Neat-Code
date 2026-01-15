#Question - https://neetcode.io/problems/two-integer-sum-ii/question

#Brute Force 
#Time Complexity: O(n**2)
def twoSum(numbers: list[int], target: int) -> list[int]:

    for i in range (0, len(numbers)):

        number_to_search = target - numbers[i]

        if number_to_search in numbers:

            return [i+1, numbers.index(number_to_search) + 1]

#Can solve using Binary search