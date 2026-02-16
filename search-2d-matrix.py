#Question -> https://neetcode.io/problems/search-2d-matrix/question?list=neetcode150

#Time Complexity: O(n)
def searchMatrix_BruteForce(matrix: list[list[int]], target: int) -> bool:

    matrix_list = []

    for m_row in matrix:
        for value in m_row:
            matrix_list.append(value)
        
    left, right = 0, len(matrix_list) - 1

    while left <= right:

        mid = (left + right) // 2

        if matrix_list[mid] == target:
            return True

        elif matrix_list[mid] < target:
            left = mid + 1
            
        else:
            right = mid - 1
        
    return False
            

#Time complexity: O(log(m*n)). Optimal Solution
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        matrix_list = []

        l, r = 0, len(matrix) - 1

        #binary search the matrix list and find the list to pass down to do binary search again.
        while l <= r:
           
            m = (l + r) // 2

            if matrix[m][0] <= target <= matrix[m][-1]:
                matrix_list = matrix[m]
                break
            
            elif matrix[m][-1] < target:
                l = m + 1
            
            else:
                r = m - 1 

        left, right = 0, len(matrix_list) - 1

        while left <= right:

            mid = (left + right) // 2

            if matrix_list[mid] == target:
                return True

            elif matrix_list[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return False
            
            

#testing
#searchMatrix_BruteForce(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10)

sol = Solution()
result = sol.searchMatrix(
        matrix=[[1,2,4,8],[10,11,12,13],[14,20,30,40]],
        target=10
    )
print(result)

            