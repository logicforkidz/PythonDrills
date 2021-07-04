'''
Given an integer n, return any list containing n unique integers such that they sum up to 0.

Example 1:
Input: n = 5
Output: [0,-1,1,-2,2]
Explanation: The sum of all elements in the above list adds upto zero.

Example 2:
Input: n = 3
Output: [0,-1,1]

Example 3:
Input: n = 2
Output: [1,-1]
'''


def zeroSumList(length):
    zeroList = []

    #if length is odd then let the first element be zero
    if (length % 2) != 0:
        zeroList.append(0)

    #add +ve  and corresponding -ve number as many times as needed to the list.
    for n in range(1, length//2+1):
        zeroList.append(n)
        zeroList.append (-1*n)
    return zeroList


if __name__ == '__main__':
    print(0, zeroSumList(0))
    print(1, zeroSumList(1))
    print(2, zeroSumList(2))
    print(3, zeroSumList(3))
    print(4, zeroSumList(4))
    print(5, zeroSumList(5))
    print(6, zeroSumList(6))
    print(7, zeroSumList(7))
    print(8, zeroSumList(8))
    print(9, zeroSumList(9))