#Three sum -> https://neetcode.io/problems/three-integer-sum/question
#Brute Force method 
#Time complexity: O(n**4)
#Space complexity: O(n**2)
def threeSum_bruteforce(nums: list[int]) -> list[list[int]]:

    triplets = []

    for i in range(len(nums) - 2):
        for j in range(i+1, len(nums) - 1):
            for k in range(j+1, len(nums)):

                if nums[i] + nums[j] + nums[k] == 0:

                    if sorted([nums[i], nums[j], nums[k]]) in triplets:
                        continue
                    else:
                        triplets.append(sorted([nums[i], nums[j], nums[k]]))
        
    return triplets


#O(n**2) method
"""
Algorithm:
    - For every number in the list do a two sum check with the number itself (two pointer)
    - Example: [-1,0,1,2,-1,-4] after it's sorted it becomes [-4,-1,-1,0,1,2]
    - First iteration = -4 [-1,-1,0,1,2] - solve two sum
    - Make sure you skipped duplicates by checking it's previous number.
"""
def threeSum(nums: list[int]) -> list[list[int]]:

    #sorting to identify duplicates and predict the increase and decrease
    nums.sort()

    triplets = []

    for i, a in enumerate(nums):

        if a > 0: #if value is positive the addition will never sum to zero. No point in searching
            break
        
        if i > 0 and nums[i] == nums[i-1]: #skipping visited value for duplicates
            continue

        l, r = i+1, len(nums) - 1

        while l < r:

            if a + nums[l] + nums[r] > 0:
                r -=1
            
            elif a + nums[l] + nums[r] < 0:
                l +=1
            
            else:
                triplets.append([a, nums[l], nums[r]])
                l +=1
                r -=1

            while l < r and nums[l] == nums[l-1]: #skipping duplicates within two sum problem and making sure both pointers never crossed each other
                l+=1
    
    return triplets
            

print(threeSum(nums=[-1,0,1,2,-1,-4]))


