'''
https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
from typing import List


class Solution_1:
    def twoSum_singleLoop(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            if target-nums[i] in nums and nums.index(target-nums[i]) != i:
                return [i, nums.index(target-nums[i])]
        return -1


    '''
    Learned how to use hashmap in python. Pretty simple. The solution itself was inspire by a LeetCoder.
    The hashmap is populated as we iterate through the loop. After we find a value which has another value
    in the map that add up to the target we return both indices.
    
    The interesting thing is this solution gives us better runtime even though the logic is same and for
    both the solution I have used early stopping.
    
    This is because the first solution contains a function named index(). This function iterates from 0 to n
    to find the index for specific value. That makes my first solution to have a complexity O(n^2).
    But for using hashmap removes this lookup cost drastically as looking up anything in a map has an amortized
    cost of O(1). So, the complexity becomes O(n).
    '''
    def twoSum_hashMap(self, nums: List[int], target: int) -> List[int]:
        s_map = {}
        for i, v in enumerate(nums):
            if target - v in s_map:
                return [s_map[target-v], i]
            s_map[v] = i

        return -1


solution = Solution_1()
nums = [int(num) for num in input().split()]
print(solution.twoSum_singleLoop(nums, int(input())))
print(solution.twoSum_hashMap(nums, int(input())))
