"""
Problem Description
Given two integers A and B, find a number X such that A xor X is minimum possible, and the number of set bits in X equals B.

Problem Constraints
0 <= A <= 109
0 <= B <= 30

Input Format
First argument contains a single integer A. Second argument contains a single integer B.

Output Format
Return a single integer X.

Example Input
Input 1:
 A = 3
 B = 3

Input 2:
 A = 15
 B = 2

Example Output
Output 1:
 7

Output 2:
 12

Example Explanation
Explanation 1:
 3 xor 7 = 4 which is minimum

Explanation 2:
 15 xor 12 = 3 which is minimum

"""
# Approch1


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        x = 0
        for i in range(30, -1, -1):
            is_set = (A & (1 << i)) > 0
            if is_set and B > 0:
                x = x | (1 << i)
                B -= 1

        for j in range(0, 31, 1):
            is_unset = (A & (1 << j)) == 0
            if is_unset and B > 0:
                x = x | (1 << j)
                B -= 1

        return x

# Approch2


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        x = 0
        for i in range(30, -1, -1):
            is_set = ((A & (1 << i)) > 0)
            if is_set:
                if B > 0:
                    x = x | (1 << i)
                    B -= 1
                else:
                    break

        bit = 0
        while B > 0:
            is_set = ((x & (1 << bit)) > 0)
            if not is_set:
                x = x | (1 << bit)
                B = B-1
            bit += 1
        return x
