'''
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]


Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n


Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
'''

from typing import List


class Solution_448:
    '''
    This was my initial solution. Pretty simple. Made a list that we can say was our goal but then
    in the input we have duplicates so we have to find the missing values. I have used a loop to find it.
    This one was NOT ACCEPTED! It went pass the time limit.
    '''
    def findDisappearedNumbers_loop(self, nums: List[int]) -> List[int]:
        actual = list(range(1, len(nums)+1))
        missing = []
        for val in actual:
            if val not in nums:
                missing.append(val)

        return missing


    '''
    Next I figured out I can use their difference. The solution below actually finds difference of 2 sets.
    It was accepted however, it is not the best solution out there. I think goal here is to somehow use the
    same list and not use any additional list:actual.
    '''
    def findDisappearedNumbers_accepted(self, nums: List[int]) -> List[int]:
        actual = list(range(1, len(nums) + 1))

        return list(set(actual).difference(set(nums)))


    '''
    This is one of the solution that I found in the solutions in LeetCode. The solution is pretty straight-forward
    yet powerful. Standing in the current position, I am trying to see if I belong here or not, if we belong we do nothing
    else we try to find an appropriate position if it also has a value that does not belong there. The solver says
    he used the list as a hashmap. Learned something new. The link to the solution can be found here:
    https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/solutions/5025659/beats-sc-o-1-tc-o-n-hash-table-cycle-sort-ppt-explanation/
    '''
    def findDisappearedNumbers_better(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):

            if nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                print("swapping "+str(nums[i])+" and "+ str(nums[nums[i] - 1]))
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                print(nums)
            else:
                i += 1

        return [i + 1 for i in range(len(nums)) if nums[i] != i + 1]


solution = Solution_448()
nums = [int(items) for items in input().split()]
print(solution.findDisappearedNumbers_loop(nums))
print(solution.findDisappearedNumbers_accepted(nums))
print(solution.findDisappearedNumbers_better(nums))
