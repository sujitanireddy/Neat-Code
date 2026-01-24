#Subset Sum Problem

def subset_sum(nums, target):

    return find_subset_sum(nums, target, len(nums)-1)


def find_subset_sum(nums, target, index):

    if target == 0:
        return True

    if index < 0 and target != 0:
        return False

    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)

    result = find_subset_sum(nums, target, index - 1)

    result_2 = find_subset_sum(nums, target - nums[index], index -1)

    if result == True or result_2 == True:

        return True

    else:
        return False

    