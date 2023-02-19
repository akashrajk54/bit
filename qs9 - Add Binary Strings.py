"""
Problem Description
Given two binary strings A and B. Return their sum (also a binary string).

Problem Constraints
1 <= length of A <= 105
1 <= length of B <= 105
A and B are binary strings

Input Format
The two argument A and B are binary strings.

Output Format
Return a binary string denoting the sum of A and B

Example Input
Input 1:
A = "100"
B = "11"
Input 2:
A = "110"
B = "10"

Example Output
Output 1:
"111"
Output 2:
"1000"

Example Explanation
For Input 1:
The sum of 100 and 11 is 111.

For Input 2:
The sum of 110 and 10 is 1000.
"""


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def str_to_num(self, A):
        a = 0
        A = A[::-1]
        for i in range(len(A)):
            val = int(A[i])
            is_set = (val & 1) > 0
            if is_set:
                a = a | (1 << i)
        return a

    def num_to_str(self, sum_val):
        ans = ''
        while sum_val > 0:
            is_set = (sum_val & 1) > 0
            if is_set:
                ans += '1'
            else:
                ans += '0'
            sum_val = sum_val >> 1
        ans = ans[::-1]
        return ans

    def addBinary(self, A, B):

        a = self.str_to_num(A)
        b = self.str_to_num(B)
        sum_val = a+b

        ans = self.num_to_str(sum_val)

        return ans
