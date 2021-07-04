'''
Write a function that:
 1. returns 1 is the product of all numbers in a list is +ve
 2. returns -1 is the product of all numbers in a list is -ve
 3. returns 0 is the product of all numbers in a list is 0

Example 1:
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Example 2:
Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0

Example 3:
Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
'''

# Algorithm: We will walk the list and 
def signProduct(numList):
    #write your code here
    return -1

if __name__ == "__main__":
    nums   = [-1,-2,-3,-4,3,2,1]
    print(f"Input{nums}, Output:", signProduct(nums))

    nums   = [1,5,0,2,-3]
    print(f"Input{nums}, Output:", signProduct(nums))

    nums   = [-1,1,-1,1,-1]
    print(f"Input{nums}, Output:", signProduct(nums))
