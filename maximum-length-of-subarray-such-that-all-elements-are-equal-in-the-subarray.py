#Question -> https://www.geeksforgeeks.org/dsa/maximum-length-of-subarray-such-that-all-elements-are-equal-in-the-subarray/


#without sliding window algo
def maximum_length_of_subarray(nums = [4,2,2,2,1,1]):

    max_length_seen = 1
    max_length = 0

    for i in range(1, len(nums)):

        if nums[i] == nums[i-1]:
            max_length_seen += 1
        
        else:
            max_length = max(max_length, max_length_seen)
            max_length_seen = 1

    return max_length

print(maximum_length_of_subarray())