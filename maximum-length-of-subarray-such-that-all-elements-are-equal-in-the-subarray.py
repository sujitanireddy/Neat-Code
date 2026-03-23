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

#with sliding window algorithm
def maximum_length_of_subarray_sliding_window(nums = [4,2,2,2,1,1]):

    L = 0
    max_length = 0

    for R in range(len(nums)):

        if nums[L] != nums[R]:

            L = R
        
        max_length = max(max_length, (R - L) + 1)
    
    return max_length
    




print(maximum_length_of_subarray_sliding_window())