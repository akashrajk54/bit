"""
Problem Description
Given a positive integer A, the task is to count the total number of set bits in the binary representation of all the numbers from 1 to A.

Return the count modulo 109 + 7.

Problem Constraints
1 <= A <= 109

Input Format
First and only argument is an integer A.

Output Format
Return an integer denoting the ( Total number of set bits in the binary representation of all the numbers from 1 to A )modulo 109 + 7.

Example Input
Input 1:
 A = 3
Input 2:
 A = 1

Example Output
Output 1:
 4
Output 2:
 1

"""


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, N):
        MOD = 10**9 + 7
        two = 2
        ans = 0
        n = N
        while (n != 0):
            ans += int(N / two) * (two >> 1)
            if ((N & (two - 1)) > (two >> 1) - 1):
                ans += (N & (two - 1)) - (two >> 1) + 1
            two <<= 1
            n >>= 1
        ans = ans % MOD
        return ans
