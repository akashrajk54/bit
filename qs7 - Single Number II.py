"""
Problem Description
Given an array of integers, every element appears thrice except for one, which occurs once.

Find that element that does not appear thrice.
NOTE: Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Problem Constraints
2 <= A <= 5*106
0 <= A <= INTMAX

Input Format
First and only argument of input contains an integer array A.

Output Format
Return a single integer.

Example Input
Input 1:
A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]

Input 2:
A = [0, 0, 0, 1]

Example Output
Output 1:
4

Output 2:
1

Example Explanation
Explanation 1:
4 occurs exactly once in Input 1.
1 occurs exactly once in Input 2.

"""
# Approch 1


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        # Elements comming 3 time having 3x value for its set bit pos, if not 3x means that setbit also present in ans
        ans = 0
        for pos in range(32):
            cnt = 0
            for each in A:
                is_set = (each & (1 << pos)) > 0
                if not is_set:
                    continue
                cnt += 1

            if cnt % 3 != 0:
                ans = ans | (1 << pos)
        return ans
