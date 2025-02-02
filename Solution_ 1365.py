'''
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.



Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]


Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100
'''
import time
from typing import List


class Solution_1365:
    '''
    The solution here is simple. As we iterate over the given list after sorting it, we keep counting and keep the count
    in a hashmap. Then we iterate over the original list to give the required output and values are chosen from the
    hashmap. While this solution solves the problem in O(n), it requires some extra space to store the sorted list,
    hashmap and the returned list. Space is cheaper than time so this is an effective solution.
    '''
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        counter = 0
        storage = {}
        for i, v in enumerate(sorted_nums):
            if sorted_nums[i-1] != sorted_nums[i]:
                storage[sorted_nums[i-1]] = counter
                counter = i
        storage[sorted_nums[len(sorted_nums)-1]] = counter

        output = []
        for val in nums:
            output.append(storage[val])

        return output

    '''
    This solution was done being inspired from an youtube to make it more efficient in terms of space while maintaining
    time complexity of O(n). However, it generated similar output for almost same space complexity. That is because the
    space for storage is still needed and the space taken by the map is almost nothing compared to the huge list of size
    102 (values can be 0<=v<=100; 2 extra for 0 and 100)
    '''
    def smallerNumbersThanCurrent_space(self, nums: List[int]) -> List[int]:
        storage = [0]*102
        for i, v in enumerate(nums):
            storage[nums[i]] += 1
        for i, v in enumerate(storage):
            storage[i] += storage[i-1]

        return [0 if v == 0 else storage[v-1] for v in nums]

solution = Solution_1365()
nums = [int(val) for val in input().split()]

start_time = time.time()
print(solution.smallerNumbersThanCurrent(nums))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(solution.smallerNumbersThanCurrent_space(nums))
print("--- %s seconds ---" % (time.time() - start_time))
