#Question -> https://neetcode.io/problems/binary-search/question?list=neetcode150

class Solution:
    def search(self, nums: list[int], target: int) -> int:

        L, R = 0, len(nums) - 1

        while L <= R:

            M = (L + R) // 2

            if nums[M] < target:
                L = M + 1

            elif nums[M] > target:
                R = M - 1

            else:
                return M

        return -1
        