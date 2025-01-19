# https://leetcode.com/problems/contains-duplicate/description/

'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true



Constraints:

1 <= nums.length <= 10^5
-109 <= nums[i] <= 10^9'''
from typing import List


class Solution_217:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for num in nums:
            numSet.add(num)

        duplicateExists = False
        if len(numSet) != len(nums):
            duplicateExists = True

        return duplicateExists

    def containsDuplicate_better(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)): return True
        else: return False

str = input()
nums = [int(item) for item in str.split()]
sol = Solution_217()
print(sol.containsDuplicate(nums))
print(sol.containsDuplicate_better(nums))