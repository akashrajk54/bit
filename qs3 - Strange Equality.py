""""
Problem Description
Given an integer A.
Two numbers, X and Y, are defined as follows:

X is the greatest number smaller than A such that the XOR sum of X and A is the same as the sum of X and A.
Y is the smallest number greater than A, such that the XOR sum of Y and A is the same as the sum of Y and A.
Find and return the XOR of X and Y.

NOTE 1: XOR of X and Y is defined as X ^ Y where '^' is the BITWISE XOR operator.
NOTE 2: Your code will be run against a maximum of 100000 Test Cases.

Problem Constraints
1 <= A <= 109

Input Format
First and only argument is an integer A.

Output Format
Return an integer denoting the XOR of X and Y.

Example Input
A = 5

Example Output
10

Example Explanation
The value of X will be 2 and the value of Y will be 8. The XOR of 2 and 8 is 10.

"""

import sys

# BF:


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        x = 0
        y = 0

        max_int = sys.maxsize
        min_int = -sys.maxsize
        for k in range(A-1, min_int, -1):
            if (A ^ k) == (A+k):
                x = k
                break

        for j in range(A+1, max_int):
            if (A ^ j) == (A+j):
                y = j
                break

        ans = x ^ y
        return ans

# Optimized approch:


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        x = 0

        # I want the ending set bit position of A
        idx_y = 0
        for j in range(32):
            if A & (1 << j) != 0:
                idx_y = j

        new_val = 0
        # hit every bit of A
        for i in range(idx_y):
            if A & (1 << i) != 0:
                pass
            else:
                new_val = (2**i)
                x += new_val

        y = 2**(idx_y+1)
        # print('x: ', x, ' y: ', y)
        ans = x ^ y
        return ans
