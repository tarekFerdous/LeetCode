#https://leetcode.com/problems/missing-number/description/?submissionId=1513013609

'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.








Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.


Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''
from typing import List


class Solution_268:
    def missingNumber_math(self, nums: List[int]) -> int:
        return int((len(nums)/2)*(len(nums)-1)+len(nums) - sum(nums))


nums = [int(item) for item in input().split()]
solution = Solution_268()
print(solution.missingNumber_math(nums))

'''
The solution used a summation formula. The formula can be given as:

Sum = n/2*(a+(n-1)*d)

Here,
n = Total number of terms
a = First term
d = Distance between each term

The formula was modified a little bit to serve purpose.

For an input of 9 6 4 2 3 5 7 0 1,
n = 9
a = 0
d = 1
This gives you all the sum from 0 to 8. So, I have added the last number which was len(nums).

Or, this could be done by a specialization of the formula which is,
Sum of first n = (n*(n-1))/2
'''