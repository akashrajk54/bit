"""
Problem Description
Given an array of positive integers A, two integers appear only once, and all the other integers appear twice.
Find the two integers that appear only once.

Note: Return the two numbers in ascending order.

Problem Constraints
2 <= |A| <= 100000
1 <= A[i] <= 10^9

Input Format
The first argument is an array of integers of size N.

Output Format
Return an array of two integers that appear only once.

"""

# Approch1:


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)

        # find xor of all
        xor_all = 0
        for i in range(n):
            xor_all = xor_all ^ A[i]

        # get the 1st set bit index of xor_all
        idx = 0
        for i in range(32):
            if xor_all & (1 << i) != 0:
                idx = i
                break

        first_val = 0
        second_val = 0
        for i in range(n):
            val = A[i]
            if val & 1 << idx != 0:
                # set
                first_val = first_val ^ val
            else:
                # unset
                second_val = second_val ^ val
        if second_val > first_val:
            ans = [first_val, second_val]
        else:
            ans = [second_val, first_val]
        return ans

# Approch:2


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        B = sorted(A)

        ans = []
        n = len(A)
        i = 0
        if len(B) >= 4:
            while i < n-2:
                if B[i] ^ B[i+1] != 0:
                    ans.append(B[i])
                    i += 1
                else:
                    i = i+2
            if len(ans) == 1:
                ans.append(B[-1])
            return ans
        else:
            return A
