'''
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0

Example 3:
Input: grid = [[1,-1],[-1,-1]]
Output: 3

Example 4:
Input: grid = [[-1]]
Output: 1
'''

# INPUT: grid is a list of list as shown above
# OUTPUT: should return a count of -ve numbers in the grid.
def countNegative(grid):
    # write your code here
    return 0


if __name__ == "__main__":
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print (countNegative(grid), grid)

    grid = [[3, 2], [1, 0]]
    print (countNegative(grid), grid)

    grid = [[1, -1], [-1, -1]]
    print (countNegative(grid), grid)

    grid = [[-1]]
    print (countNegative(grid), grid)
