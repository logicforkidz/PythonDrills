'''
Running Sum of 1d Array

Given a list of nums. We define a running sum as a list of numbers
such that each element in the output list is equal to the sum of all
elements upto that position in the input list.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

'''

def runningSum(nums):
    sum = []
    return sum

if __name__ == "__main__":
    print(runningSum([1,2,3,4]))
    print (runningSum([3,1,2,10,1]))
    print(runningSum([]))
